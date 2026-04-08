<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const message = ref('')
const students = ref([])
const route = useRoute()

async function fetchShortlistedStudents() {
  const token = localStorage.getItem('token')
  if (!token) {
    localStorage.clear()
    window.location.href = '/login'
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:5000/company/shortlisted_students', {
      params: {
        search: (route.query.search || '').toString()
      },
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    students.value = response.data
  } catch (error) {
    if (error.response?.status === 401 || error.response?.status === 422) {
      localStorage.clear()
      window.location.href = '/login'
      return
    }
    message.value = 'failed to load shortlisted students'
  }
}

async function viewResume(application_id) {
  const token = localStorage.getItem('token')
  if (!token) {
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
  } catch (error) {
    if (error.response?.status === 401 || error.response?.status === 422) {
      localStorage.clear()
      window.location.href = '/login'
      return
    }
    message.value = error.response?.data?.message || 'failed to download resume'
  }
}

onMounted(() => {
  fetchShortlistedStudents()
})

watch(
  () => route.query.search,
  () => {
    fetchShortlistedStudents()
  }
)
</script>

<template>
  <p v-if="message">{{ message }}</p>
  <div>
    <h1>Shortlisted Students</h1><br>
    <table v-if="students.length > 0">
      <thead>
        <tr>
          <th>Application ID</th>
          <th>Drive ID</th>
          <th>Job Title</th>
          <th>Student ID</th>
          <th>Student Name</th>
          <th>Student Email</th>
          <th>Apply Date</th>
          <th>Resume</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stu in students" :key="stu.application_id">
          <td>{{ stu.application_id }}</td>
          <td>{{ stu.drive_id }}</td>
          <td>{{ stu.job_title }}</td>
          <td>{{ stu.student_id }}</td>
          <td>{{ stu.student_name }}</td>
          <td>{{ stu.student_email }}</td>
          <td>{{ stu.application_date }}</td>
          <td>
            <button @click="viewResume(stu.application_id)" :disabled="!stu.resume_path">view resume</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>no shortlisted students found</p>
  </div>
</template>

<style scoped>
h1 {
  color: #2980B9;
}
</style>
