<script setup>


import { ref, onMounted } from 'vue'
import api from '@/services/api'

const message = ref('')
const drives = ref([])
const past_drives=ref([])


// fetching drives ________________
// with get request

function pastDrives(drives) {
    const today = new Date()

    return drives.filter(drive => {
        const deadline = new Date(drive.application_deadline)
        return deadline < today
    })
}

const fetchDrives = async () => {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return}

    try{
        message.value = ' '
        const response = await api.get(
            '/drives',
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        drives.value = response.data
        past_drives.value = pastDrives(response.data)
    } catch (error) {
        console.error(error)
        if (error.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = "Failed to load drives"
    }
}

// END of fetch drives with get_______________________

onMounted(() => {
    fetchDrives()
})
</script>
<template>
    
    <p v-if="message">{{ message }}</p>
            <div id="all_drives">
                <h1>Past Drives</h1><br>
                <div class="table">
                    <table v-if="past_drives.length>0">
                    <thead>
                        <tr>
                        <th>Drive ID</th>
                        <th>Company ID</th>
                        <th>Job Title</th>
                        <th>Job Description</th>
                        <th>Branch</th>
                        <th>Year</th>
                        <th>Deadline</th>
                    </tr>
                    </thead>
                    <tbody>

                    <tr v-for="drive in past_drives" :key="drive.drive_id">
                        <td>{{ drive.drive_id }}</td>
                        <td>{{ drive.company_id }}</td>
                        <td>{{ drive.job_title }}</td>
                        <td>{{ drive.job_description }}</td>
                        <td>{{ drive.branch }}</td>
                        <td>{{ drive.year }}</td>
                        <td>{{ drive.application_deadline }}</td>
                    </tr>
                    </tbody>
                    </table>
                    <p v-else>no records</p>
                </div>
            </div>
</template>
<style scoped>
#all_drives{
    color: #2980B9;
    margin-top: 30px;
}

</style>