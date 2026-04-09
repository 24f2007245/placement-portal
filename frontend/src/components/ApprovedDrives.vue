<script setup>


import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')
const drives = ref([])


// fetching drives ________________
// with get request

const fetchDrives = async () => {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return}

    try{
        const response = await axios.get(
            'http://127.0.0.1:5000/drives',
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        drives.value = response.data
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
                <h1>Placements Drives</h1><br>
                <div class="table">
                    <table>
                    <tr>
                        <th>Drive ID</th>
                        <th>Company ID</th>
                        <th>Job Title</th>
                        <th>Job Description</th>
                        <th>Branch</th>
                        <th>Year</th>
                        <th>Deadline</th>
                    </tr>

                    <tr v-for="drive in drives" :key="drive.drive_id">
                        <td>{{ drive.drive_id }}</td>
                        <td>{{ drive.company_id }}</td>
                        <td>{{ drive.job_title }}</td>
                        <td>{{ drive.job_description }}</td>
                        <td>{{ drive.branch }}</td>
                        <td>{{ drive.year }}</td>
                        <td>{{ drive.application_deadline }}</td>
                    </tr>
                    </table>
                </div>
            </div>
</template>
<style scoped>
#all_drives{
    color: #2980B9;
    margin-top: 30px;
}

</style>