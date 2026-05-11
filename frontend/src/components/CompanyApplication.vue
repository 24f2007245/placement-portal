<script setup>


import api from '@/services/api'
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

const users = ref([])
const route = useRoute()
const message = ref('')




const fetchUsers = async () => {
    const token = localStorage.getItem('token')
    if (!token){
        window.location.href = '/login'
        return}

    try{
        const response = await api.get(
            '/company_application',
            {
                params: {
                    search: (route.query.search || '').toString()
                },
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        users.value = response.data
    } catch (err) {
        if (err.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        console.log(err)
    }
}



const approveApplication = async (user_id) => {
    const token = localStorage.getItem('token')
    if(!token) {
        window.location.href = '/login'
        return
    }

    try{
        const response = await api.patch(
            `/approve_application/${user_id}`,
            { status: 1 },
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        console.log(response.data)

        fetchUsers()
    } catch (err) {
        if (err.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return}
        console.log(err.response ? err.response.data : err)
    }
}

const removeCompany = async (user_id) => {
    const token = localStorage.getItem('token')
    if(!token) {
        window.location.href = '/login'
        return}

    try{
        const response = await api.delete(
            `/admin/remove_company/${user_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        message.value = response.data?.message || 'company removed successfully'
        fetchUsers()
    } catch(err) {
        if (err.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'failed to remove company'
    }
}

onMounted(() => {
    fetchUsers()
})

watch(
    () => route.query.search,
    () => {
        fetchUsers()
    }
)
</script>

<template>
    <p v-if="message">{{ message }}</p>
    <p style="color: chocolate;">Total Number Of Company/Recruiter For Registration is {{ users.length }}</p>

    <div id="company_application">
        <h1>Company Application</h1><br>
        <div id="cntnt">
            <div class="table">
                <table v-if="users.length>0">
                <thead>
                    <tr>
                    <th>Company ID</th>
                    <th>Company Name</th>
                    <th>Company Email</th>
                    <th>Approve</th>
                    <th>Remove</th>
                </tr>
                </thead>

                <tbody>
                    <tr v-for="user in users" :key="user.user_id">
                    <td>{{ user.user_id }}</td>
                    <td>{{ user.user_name }}</td>
                    <td>{{ user.user_email }}</td>
                    <td><button @click="approveApplication(user.user_id) ">approve</button></td>
                    <td><button class="dngr" @click="removeCompany(user.user_id)">remove</button> </td>
                </tr>
                </tbody>
                </table>
                <p v-else>no records</p>
            </div>
        </div>
        </div>
</template>

<style scoped>
#company_application{
    
    margin-top: 30px;
}
/* #cntnt{
    border: 1px solid #2980B9;
    padding: 30px;
} */

 .dngr{
    color: red;
 }
</style>
