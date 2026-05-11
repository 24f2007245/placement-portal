<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/services/api'
const rcusers = ref([])
const route = useRoute()
const message = ref('')



// fetching company
// get request

const fetchUsers = async () => {
    try {
        const response = await api.get(
            '/admin/registered_company',
            {
                params: {
                    search: (route.query.search || '').toString()
                },
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            }
        )

        rcusers.value = response.data
    } catch (err) {
        console.log(err)
    }
}

function blackList(){
    return
}


// delete request 
// deleting company____________________

async function removeCompany(user_id) {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

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
    } catch (err) {
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
    <div id="registered_company">
        <p v-if="message">{{ message }}</p>
        <p style="color: chocolate;">Total Number Of Registered Company/Recruiter is {{ rcusers.length }}</p>

        <h1>Registered Companys</h1><br>
        <div class="table">
            <table>
            <thead>
                <tr>
                    <th>Company ID</th>
                    <th>Company Name</th>
                    <th>Company Email</th>
                    <th>Blacklist</th>
                    <th>Remove</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="user in rcusers" :key="user.user_id">
                    <td>{{ user.user_id }}</td>
                    <td>{{ user.user_name }}</td>
                    <td>{{ user.user_email }}</td>
                    <td>
                        <button class="dngr" @click="blackList(user.user_id)">
                            blacklist
                        </button>
                    </td>
                    <td>
                        <button class="dngr" @click="removeCompany(user.user_id)">remove</button>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>
<style>


#registered_company {
    margin-top: 30px;
}

#dngr {
    color: red;
}
</style>