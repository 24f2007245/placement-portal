<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
const rcusers = ref([])
const fetchUsers = async () => {
    try {
        const response = await axios.get(
            'http://127.0.0.1:5000/admin/registered_company',
            {
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

onMounted(() => {
    fetchUsers()
})
</script>

<template>
    <div id="registered_company">
        <p style="color: chocolate;">Total Number Of Registered Company/Recruiter is {{ rcusers.length }}</p>

        <h1>Registered Companys</h1><br>
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
                        <button class="dngr">remove</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<style>
table {
    border-collapse: collapse;
    /* color: gray; */
}

td {
    color: gray;
    padding: 5px;
}

th {
    padding: 5px;
}

#registered_company {
    margin-top: 30px;
}

#dngr {
    color: red;
}
</style>