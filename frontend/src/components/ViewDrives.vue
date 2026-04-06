<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')

const drives = ref([])
const drives_awaiting = ref([])
const drives_approved = ref([])

function subDescription(description) {
    if (!description) {
        return '-'
    }
    if (description.length > 100) {
        return description.slice(0, 100) + '...'
    }
    return description
}

const fetchDrives = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get(
            'http://127.0.0.1:5000/company/drives',
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        
        drives.value = response.data
        for(let drive of drives.value){
            if(drive.status===1){
                drives_approved.value.push(drive)
            }else{
                drives_awaiting.value.push(drive)
            }
        }
        
    } catch (error) {
        console.error(error)
        if (error.response?.status === 401 || error.response?.status === 422) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = "Failed to load drives"
    }
}

onMounted(() => {
    fetchDrives()
})
</script>
<template>
    <p v-if="message">{{ message }}</p>
            <div id="drive_awaiting">
                <h1>Awaiting Drives</h1><br>
                <table v-if="drives_awaiting.length>0">
                <thead>
                    <tr>
                    <th>Drive ID</th>
                    <th>Job Title</th>
                    <th>Description</th>
                    <th>Branch</th>
                    <th>Year</th>
                    <th>CGPA</th>
                    <th>Deadline</th>
                    <th>Edit/change</th>
                </tr>
                </thead>

                <tbody>
                    <tr v-for="d in drives_awaiting" :key="d.drive_id">
                    <td>{{d.drive_id }}</td>
                    <td>{{d.job_title }}</td>
                    <td>{{ subDescription(d.job_description) }}</td>
                    <td>{{d.branch }}</td>
                    <td>{{d.year }}</td>
                    <td>{{d.cgpa }}</td>
                    <td>{{d.application_deadline  }}</td>
                    <td><button>edit/change</button></td>
                </tr>
                </tbody>
                </table>
                <p v-else>no records found</p>
            </div>
            <div id="approved_drives">
                <h1>Your Approved Drives</h1><br>
                <table v-if="drives_approved.length>0">
                <thead>
                    <tr>
                    <th>Drive ID</th>
                    <th>Job Title</th>
                    <th>Description</th>
                    <th>Branch</th>
                    <th>Year</th>
                    <th>CGPA</th>
                    <th>Deadline</th>
                    <th>Edit/change</th>
                </tr>
                </thead>

                <tbody>
                    <tr v-for="drive in drives_approved" :key="drive.drive_id">
                    <td>{{ drive.drive_id }}</td>
                    <td>{{ drive.job_title }}</td>
                    <td>{{ subDescription(drive.job_description) }}</td>
                    <td>{{ drive.branch }}</td>
                    <td>{{ drive.year }}</td>
                    <td>{{ drive.cgpa }}</td>
                    <td>{{ drive.application_deadline  }}</td>
                    <td><button>edit/change</button></td>
                </tr>
                </tbody>
                </table>
                <p v-else>no records found</p>
            </div>
</template>
<style scoped>
#approved_drives{
    /* color: #2980B9; */
    margin-top: 20px;
    /* overflow: hidden; */
    /* margin-top: 30px;
    margin-right: 20px; */
    /* overflow:scroll; */
    
}
#drive_awaiting{
    margin-top: 20px;
}

#drive_awaiting,
#approved_drives {
    overflow-x: auto;
}

table{
    width: 100%;
    min-width: 760px;
    border-collapse: collapse;
}

th,
td {
    padding: 8px 10px;
    /* white-space: nowrap; */
}

h1{
    color: #2980B9;
}

</style>