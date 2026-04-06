<script setup>
import { ref } from 'vue'
import axios from 'axios'

const students = ref({

    student_id: '',
    phone_no: '',
    address: '',
    social_profile: '',
})

const resumeFile = ref(null)
const message = ref('')

async function fetchStudents() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get('http://localhost:5000/student_profile', {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        // backend returns either profile object or message object
        if (response.data?.student_id !== undefined) {
            students.value = response.data
            message.value = ''
        } else {
            message.value = response.data?.message || ''
        }
    } catch (err) {
        if (err.response?.status === 401) {
            message.value = 'Token expired, please relogin'
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'Failed to fetch profile'
        console.error(err)
    }
}

function onFileChange(event) {
    resumeFile.value = event.target.files?.[0] || null
}

async function downloadResume() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get('http://localhost:5000/student_profile/resume', {
            headers: {
                Authorization: `Bearer ${token}`,
            },
            responseType: 'blob',
        })

        const blobUrl = URL.createObjectURL(response.data)
        const anchor = document.createElement('a')
        anchor.href = blobUrl
        anchor.download = `resume_${students.value.student_id || 'student'}.pdf`
        document.body.appendChild(anchor)
        anchor.click()
        document.body.removeChild(anchor)
        URL.revokeObjectURL(blobUrl)
        message.value = 'Resume downloaded successfully'
    } catch (err) {
        if (err.response?.status === 401) {
            message.value = 'Token expired, please relogin'
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'Failed to download resume'
        console.error(err)
    }
}

async function updateStudent() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    const formData = new FormData()
    formData.append('student_id', students.value.student_id)
    formData.append('phone_no', students.value.phone_no)
    formData.append('address', students.value.address)
    formData.append('social_profile', students.value.social_profile)

    if (resumeFile.value) {
        formData.append('resume', resumeFile.value)
    }

    try {
        const response = await axios.put('http://localhost:5000/student_profile', formData, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        message.value = response.data?.message || 'Updated successfully'
        await fetchStudents()
    } catch (err) {
        if (err.response?.status === 401) {
            message.value = 'Token expired, please relogin'
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = err.response?.data?.message || 'Update failed'
        console.error(err)
    }
}

fetchStudents()
</script>

<template>
    <div>
        <h1>Student Profile</h1>
        <p v-if="message" class="msg">{{ message }}</p>

        <form @submit.prevent="updateStudent">
            <p>Student Id: {{ students.student_id }}</p>

            <label for="file">Upload Resume</label><br />
            <input type="file" id="file" accept=".pdf" placeholder="pdf files" @change="onFileChange" >
            <button type="button" @click="downloadResume">download current resume</button>
            <p class="note">*Only PDF files are acceptable.</p><br />

            <label for="phone">Phone No</label><br />
            <input type="tel" id="phone" placeholder="your phone number" v-model="students.phone_no" /><br />

            <label for="address">Address</label><br />
            <textarea name="address" id="address" cols="55" rows="3" placeholder="Enter your full address here"
                v-model="students.address"></textarea><br />

            <label for="social_profile">Social Profile</label><br />
            <input type="text" id="social_profile" placeholder="https://linkedin.in/example"
                v-model="students.social_profile" /><br /><br />

            <button type="submit">update</button>
        </form>
    </div>
</template>

<style scoped>
input {
    margin: 1px;
    color: gray;
    width: 250px;
    line-height: 30px;
}

label {
    color: #2980b9;
}

button {
    font-weight: bold;
    border: 2px solid cadetblue;
    text-decoration: underline;
}

textarea {
    margin: 1px;
    border: 1px solid #2980b9;
    padding: 3px;
    color: gray;
}

.msg {
    color: chocolate;
}
</style>