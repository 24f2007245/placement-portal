<script setup>
import { ref, reactive } from 'vue'
import axios from 'axios'

const formData = reactive({
  job_title: '',
  job_description: '',
  branch: '',
  cgpa: '',
  year: new Date().getFullYear(),
  application_deadline: ''
})

const message = ref('')
const loading = ref(false)

async function create_drive() {
  const token = localStorage.getItem('token')

  if (!token) {
    localStorage.clear()
    window.location.href = '/login'
    return
  }

  loading.value = true
  message.value = ''

  try {
    const response = await axios.put(
      'http://localhost:5000/drives',
      formData,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )

    message.value = 'Drive created successfully ✅'

    // Reset form
    Object.assign(formData, {
      job_title: '',
      job_description: '',
      branch: '',
      cgpa: '',
      year: new Date().getFullYear(),
      application_deadline: ''
    })

  } catch (error) {
    if (error.response?.status === 401) {
      localStorage.clear()
      message.value = 'Session expired. Please login again.'
      window.location.href = '/login'
      return
    }

  } 
}
</script>

<template>
    <div id="rest_con">
        <h1>Create Placement Drives</h1>

        <div id="drives">
            <!-- <h1>Create Placement Drive</h1> -->
            <form @submit.prevent="create_drive">

  <label>Job Title:</label>
  <input type="text" v-model="formData.job_title" required>

  <label>Job Description:</label>
  <textarea v-model="formData.job_description" required></textarea>

  <label>Branch:</label>
  <input type="text" v-model="formData.branch">

  <label>CGPA:</label>
  <input type="number" v-model="formData.cgpa" step="0.1" required>

  <label>Year:</label>
  <input type="number" v-model="formData.year" min="2000" max="2030" required>

  <label>Application Deadline:</label>
  <input type="date" v-model="formData.application_deadline" required>

  <button :disabled="loading">
    {{ loading ? 'Creating...' : 'Create' }}
  </button>

</form>

<p v-if="message">{{ message }}</p>
            <p v-if="message" class="fade">MESSAGE: {{ message }}</p>
        </div>
    </div>
</template>

<style scoped>
#drives{
    margin-top: 20px;
    /* background-color: #f5f5f5; */
    width: 100%;
    /* border-radius: 12px; */
    /* height:40vh; */
    padding-left: 30px;
    margin-bottom: 50px;
    align-self: center;
    justify-content: center;
}
input{
    padding: 5px;
    border: 1px solid #2980b9;
}
</style>