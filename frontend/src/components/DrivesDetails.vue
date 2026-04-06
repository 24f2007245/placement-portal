<script setup>
import {ref, onMounted} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import LogedinNav from './LogedinNav.vue'

const drive_detail=ref(null)
const message = ref('')
const router=useRouter()
const route=useRoute()
const drive_id=route.params.id

async function fetchDriveDetails(){
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get(
            `http://127.0.0.1:5000/drives/${drive_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        drive_detail.value = response.data
    } catch (error) {
        if (error.response?.status === 401 || error.response?.status === 422) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = error.response?.data?.message || 'Failed to load drive details'
    }
}

onMounted(() => {
    fetchDriveDetails()
})

</script>

<template>
    <LogedinNav/>
    <div id="details_wrap">
        <button @click="router.back()">Back</button>
        <p v-if="message">{{ message }}</p>

        <div v-if="drive_detail" id="card">
            <h1>Job Details</h1>
            <h3>Job Name</h3>
            <p>{{ drive_detail.job_title }}</p>
            <h3>Description</h3>
            <p>{{ drive_detail.job_description }}</p>

            <h3>About Company</h3>
            <p>Company Id: {{ drive_detail.company_id }}</p>
            <p>Know more about company <button>know more</button></p>

            <h3>Eligibility Criteria</h3>
            <p>Branch:{{ drive_detail.branch }}</p>
            <p>CGPA:{{ drive_detail.cgpa }}</p>
            <p>Year:{{ drive_detail.year }}</p>
            <p>Deadline:{{ drive_detail.application_deadline }}</p>
        </div>
    </div>

</template>

<style scoped>
#details_wrap{
    color: #2980B9;
    margin-top: 20px;
}

#card{
    margin-top: 10px;
    padding: 20px;

    /* border: 1px solid #2980B9;
    border-radius: 8px; */
    /* background-color: #f5f5f5; */
}
p{
    color: gray;
}
h3{
    margin-top: 10px;
}
</style>