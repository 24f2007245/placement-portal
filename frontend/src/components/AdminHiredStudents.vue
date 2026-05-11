<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/services/api'

const message = ref('')
const hiredStudents = ref([])
const route = useRoute()

async function fetchHiredStudents() {
  const token = localStorage.getItem('token')
  if (!token) {
    localStorage.clear()
    window.location.href = '/login'
    return
  }

  try {
    const response = await api.get('/admin/hired_students', {
      params: {
        search: (route.query.search || '').toString()
      },
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    hiredStudents.value = response.data
  } catch (error) {
    if (error.response?.status === 401 || error.response?.status === 422) {
      localStorage.clear()
      window.location.href = '/login'
      return
    }
    message.value = error.response?.data?.message || 'failed to load hired students'
  }
}

onMounted(() => {
  fetchHiredStudents()
})

watch(
  () => route.query.search,
  () => {
    fetchHiredStudents()
  }
)
</script>

<template>
  <p v-if="message">{{ message }}</p>
  <div>
    <h1>Hired Students</h1><br>
    <p style="color: chocolate;">Total Hired Students: {{ hiredStudents.length }}</p>

    <div class="table">
      <table v-if="hiredStudents.length > 0">
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
          </tr>
        </thead>
        <tbody>
          <tr v-for="stu in hiredStudents" :key="stu.application_id">
            <td>{{ stu.application_id }}</td>
            <td>{{ stu.drive_id }}</td>
            <td>{{ stu.job_title }}</td>
            <td>{{ stu.company_id }}</td>
            <td>{{ stu.student_id }}</td>
            <td>{{ stu.student_name }}</td>
            <td>{{ stu.student_email }}</td>
            <td>{{ stu.application_date }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>no hired students found</p>
    </div>
  </div>
</template>

<style scoped>
h1 {
  color: #2980B9;
}
</style>
