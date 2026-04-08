<script setup>


import {ref, reactive} from 'vue'

const formData = reactive({
    job_title: '',
    job_description: '',
    branch: '',
    cgpa: null,
    year:'',
    application_deadline: null
})

const message = ref('')

import axios from 'axios'

async function create_drive(){
    const token = localStorage.getItem('token')
    if(!token) {
        localStorage.clear()
        window.location.href = '/login'
        return}

    try{
        const response = await axios.post(
            'http://localhost:5000/drives',
            formData,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        message.value='Drives Created successfully'

    

    }catch(error){
        if (error.response?.status === 401) {
            localStorage.clear()
            message.value = 'Session expired. Please login again.'
            window.location.href = '/login'
            return
        }
        message.value = error.response?.data?.message || 'Failed to create drive'
        
    }
}

// if(response.status===200){
//     message.value='Drives Created successfully'
// }


</script>

<template>
    <div id="rest_con">
        <h1>Create Placement Drives</h1>

        <div id="drives">
            <!-- <h1>Create Placement Drive</h1> -->
            <form method="POST" @submit.prevent="create_drive">

                <label for="job_title">Job Title:</label><br>
                <input type="text" v-model="formData.job_title" id="job_title" placeholder="job title" required autocapitalize ><br>

                <label for="job_description">Job Description:</label><br>
                <textarea type="text" v-model="formData.job_description" id="job_description"
                    placeholder="job description" required rows="5" cols="50" ></textarea><br>

                <label for="branch">Branch:</label><br>
                <input type="text" v-model="formData.branch" id="branch" placeholder="branch"><br>

                <label for="cgpa">CGPA:</label><br>
                <input type="number" v-model="formData.cgpa" id="cgpa" placeholder="cgpa" step="0.1" required><br>

                <label for="year">Year:</label><br>
                <input type="number" v-model="formData.year" id="year" min="2000" max="2030" step="1" value="2025" required><br>

                <label for="application_deadline">Application Deadline:</label><br>
                <input type="date" v-model="formData.application_deadline" id="application_deadline" required><br><br>
                <button class="fix-row3">create</button>
            </form>
            <p v-if="message" class="fade">MESSAGE: {{ message }}</p>
        </div>
    </div>
</template>

<style scoped>

h1{
    color: #2980b9;
}


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
    margin: 1px;
    padding: 5px;
    border: 1px solid #2980b9;
    width: 350px;
    line-height: 30px;
}
textarea{
    margin: 1px;
    border: 1px solid #2980b9;
}
button{
    border: 2px solid cadetblue;
    font-weight: bold;
}
</style>