<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')
const applications = ref([])

function statusText(status){
    if (status === 0) return 'Applied'
    if (status === 1) return 'Shortlisted'
    if (status === 2) return 'Selected'
    if (status === 3) return 'Rejected'
}

async function fetchApplications() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get('http://127.0.0.1:5000/student/applications', {
        headers: {
            Authorization: `Bearer ${token}`
        }
        })

        applications.value = response.data

    } catch(error) {
        if (error.response?.status === 401) {
        localStorage.clear()
        window.location.href = '/login'
        return
        }
        message.value = error.response?.data?.message || 'failed to load applications'
    }
}

onMounted(() => {
    fetchApplications()
})



</script>

<template>
    <p v-if="message">{{ message }}</p>
    <div id="apps">
        <p style="color: chocolate;">Total Number Of Applications is {{ applications.length }}</p>
        <button>
            <div id="export">
            Export Your Data
        </div>
        </button>
        <h1>My Applications</h1><br>
        
        <div class="table">
        <table v-if="applications.length > 0">
        <thead>
            <tr>
            <th>Application ID</th>
            <th>Drive ID</th>
            <th>Job Title</th>
            <th>Company ID</th>
            <th>Apply Date</th>
            <th>Status</th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="app in applications" :key="app.application_id">
            <td>{{ app.application_id }}</td>
            <td>{{ app.drive_id }}</td>
            <td>{{ app.job_title }}</td>
            <td>{{ app.company_id }}</td>
            <td>{{ app.application_date }}</td>
            <td>{{ statusText(app.status) }}</td>
            </tr>
        </tbody>
        </table>
        <p v-else>no applications found</p>
        </div>
    </div>
</template>

<style scoped>
#apps {
  margin-top: 20px;
}

.export-actions {
    margin-bottom: 12px;
}

.export-actions button {
    margin-right: 8px;
}

h1 {
  color: #2980B9;
}

#export{
    padding: 10px;
    border: 1px solid #2980B9;
}

</style>
