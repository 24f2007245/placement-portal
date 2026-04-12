<script setup>


import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const message = ref('')
const applications = ref([])
const route = useRoute()
const router = useRouter()
const drive_id = route.params.id


function statusText(status) {
    if (status === 0) return 'Applied'
    if (status === 1) return 'Shortlisted'
    if (status === 2) return 'Selected'
    if (status === 3) return 'Rejected'
    }


async function fetchApplications() {
    const token =localStorage.getItem('token')
    if (!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }



    try{
        const response =await axios.get(
        `http://127.0.0.1:5000/company/drive_applications/${drive_id}`,
        {
            params: {
            search: (route.query.search || '').toString()
            },
            headers: {
            Authorization: `Bearer ${token}`
            }
        }
        )
        applications.value = response.data
    }catch(error) {
        if (error.response?.status === 401 || error.response?.status === 422) {
        localStorage.clear()
        window.location.href = '/login'
        return
        }
        message.value = error.response?.data?.message || 'failed to load applications'
    }
}

async function updateApplicationStatus(application_id, status) {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.patch(
        `http://127.0.0.1:5000/company/application_status/${application_id}`,
        { status: status },
        {
            headers: {
            Authorization: `Bearer ${token}`
            }
        }
        )

        message.value = response.data?.message || 'application status updated'
        await fetchApplications()
    } catch(error) {
        if (error.response?.status === 401) {
        localStorage.clear()
        window.location.href = '/login'
        return
        }
        message.value = error
    }
}

async function viewResume(application_id) {
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get(
        `http://127.0.0.1:5000/company/application_resume/${application_id}`,
        {
            headers: {
            Authorization: `Bearer ${token}`
            },
            responseType: 'blob'
        }
        )

        const fileURL = window.URL.createObjectURL(new Blob([response.data]))
        window.open(fileURL, '_blank')

        setTimeout(() => {
        window.URL.revokeObjectURL(fileURL)
        }, 1000)

        message.value = 'resume opened successfully'
    }catch (error) {
        if(error.response?.status === 401) {
        localStorage.clear()
        window.location.href = '/login'
        return
        }
        message.value = error.response?.data?.message || 'failed to download resume'
    }
}

onMounted(() => {
    fetchApplications()
})

watch(
    () => route.query.search,
    () => {
        fetchApplications()
    }
)
</script>

<template>
    <div>
        <button @click="router.back()">back</button>
        <p v-if="message">{{ message }}</p>
        <p style="color: chocolate;">Total Number Of Applications is {{ applications.length }}</p>
        <h1> Applications for Drive {{ drive_id }} </h1><br>
        <div class="table">
            <table v-if="applications.length > 0">
            <thead>
                <tr>
                <th> Application ID</th>
                <th> Student ID</th>
                <th> Student Name</th>
                <th> Student Email</th>
                <th> Apply Date</th>
                <th> Status</th>
                <th> Resume</th>
                <th> Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="app in applications" :key="app.application_id">
                <td>{{ app.application_id }}</td>
                <td>{{ app.student_id }}</td>
                <td>{{ app.student_name }}</td>
                <td>{{ app.student_email }}</td>
                <td>{{ app.application_date }}</td>
                <td>{{ statusText(app.status) }}</td>
                <td>
                    <button @click="viewResume(app.application_id)">view resume</button>
                </td>
                <td>
                    <button @click="updateApplicationStatus(app.application_id, 1)">shortlist</button>
                    <button @click="updateApplicationStatus(app.application_id, 3)">reject</button></td>
                </tr>
            </tbody>
            </table>

            <p v-else>no applications found for this drive</p>
        </div>
    </div>
</template>

<!-- style csss part -->

<style scoped>
h1 {
  color: #2980B9;
}
</style>
