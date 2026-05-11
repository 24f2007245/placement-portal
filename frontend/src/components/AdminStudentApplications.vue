<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/services/api'

const message = ref('')
const applications = ref([])
const route = useRoute()

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
        const response = await api.get('/admin/student_applications', {
        params: {
            search: (route.query.search || '').toString()
        },
        headers: {
            Authorization: `Bearer ${token}`
        }
        })

        applications.value = response.data
    } catch (error) {
        if (error.response?.status === 401 || error.response?.status === 422) {
        localStorage.clear()
        window.location.href = '/login'
        return
        }
        message.value = error.response?.data?.message || 'failed to load student applications'
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
    <p v-if="message">{{ message }}</p>

    <div>
        <h1>Student Applications</h1><br>
        <p style="color: chocolate;">Total Applications: {{ applications.length }}</p>

        <div class="table">
            <table v-if="applications.length > 0">
            <thead>
                <tr>
                <th>Application ID</th>
                <th>Drive ID</th>
                <th>Job Title</th>
                <th>Company ID</th>
                <th>Student ID</th>
                <th>Student Name</th>
                <th>Student Email</th>
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
                <td>{{ app.student_id }}</td>
                <td>{{ app.student_name }}</td>
                <td>{{ app.student_email }}</td>
                <td>{{ app.application_date }}</td>
                <td>{{ statusText(app.status) }}</td>
                </tr>
            </tbody>
            </table>
            <p v-else>no student applications found</p>
        </div>

        
    </div>
</template>

<style scoped>
h1 {
  color: #2980B9;
}
</style>
