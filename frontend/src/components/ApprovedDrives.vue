<script setup>


import { ref, onMounted } from 'vue'
import api from '@/services/api'
import LoadingSpinner from '@/components/LoadingSpinner.vue'

const message = ref('')
// const drives = ref([])
const active_drives=ref([])
const isLoading = ref(false)


// fetching drives ________________
// with get request

function onlyActiveDrive(drivesList) {
    const today = new Date()

    return drivesList.filter(drive => {
        const deadline = new Date(drive.deadline)
        return deadline >= today
    })
}

const fetchDrives = async () => {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return}

    try{
        isLoading.value = true
        message.value = ' '
        const response = await api.get(
            '/drives',
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        // drives.value = response.data
        active_drives.value = onlyActiveDrive(response.data)
    } catch (error) {
        console.error(error)
        if (error.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = "Failed to load drives"
    } finally {
        isLoading.value = false
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
                <div v-if="isLoading" class="inline-loader">
                    <LoadingSpinner label="Loading" />
                </div>
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

                    <tr v-for="drive in active_drives" :key="drive.drive_id">
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

.inline-loader{
    margin: 8px 0 12px;
}

</style>