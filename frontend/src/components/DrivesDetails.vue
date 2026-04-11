<script setup>

// importing ___________
import {ref, onMounted} from 'vue'
import { useRoute,useRouter } from 'vue-router'
import axios from 'axios'
import LogedinNav from './LogedinNav.vue'

const drive_detail=ref(null)

const message = ref('')
const router=useRouter()
const route=useRoute()
const drive_id=route.params.id


// fetching drives_______________________________
// get request

async function fetchDriveDetails(){
    const token = localStorage.getItem('token')
    if (!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response =await axios.get(
            `http://127.0.0.1:5000/drives/${drive_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        drive_detail.value =response.data
    }catch(error){
        if (error.response?.status === 401 || error.response?.status === 422) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = error.response?.data?.message || 'Failed to load drive details'
    }
}
// END get drives____________________________



// fetching_________________________
// get request

// async function fetchApplications(){
//     const token = localStorage.getItem('token')
//     if(!token || role !== 'admin'){
//         return
//     }

//     try{
//         const response = await axios.get(
//             `http://127.0.0.1:5000/admin/drive_applications/${drive_id}`,
//             {
//                 headers: {
//                     Authorization: `Bearer ${token}`
//                 }
//             }
//         )
//         applications.value = response.data
//     }catch(error){
//         console.error(error)
//         applications.value = []
//     }
// }


function companyDetail(company_id){
    router.push(`/company/${company_id}`)
}

onMounted(() =>{
    fetchDriveDetails()
    // fetchApplications()
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
            <p>Know more about company <button @click="companyDetail(drive_detail.company_id)">know more</button></p>

            <h3>Eligibility Criteria</h3>
            <p>Branch:{{ drive_detail.branch }}</p>
            <p>CGPA:{{ drive_detail.cgpa }}</p>
            <p>Graduating Year:{{ drive_detail.year }}</p>
            <p>Deadline:{{ drive_detail.application_deadline }}</p>
        </div>
        <!-- <hr>
        <div v-if="role === 'admin' && applications.length > 0" id="applications_section">
            <h2>Student Applications ({{ applications.length }})</h2>
            <table>
                <thead>
                    <tr>
                        <th>Student ID</th>
                        <th>Student Name</th>
                        <th>Email</th>
                        <th>Application Date</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="app in applications" :key="app.application_id">
                        <td>{{ app.student_id }}</td>
                        <td>{{ app.student_name }}</td>
                        <td>{{ app.student_email }}</td>
                        <td>{{ app.application_date }}</td>
                        <td>{{ statusText(app.status) }}</td>
                    </tr>
                </tbody>
            </table>
        </div> -->
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

#applications_section{
    margin-top: 40px;
    padding: 20px;
    /* border: 1px solid #ddd; */
    /* border-radius: 8px; */
}


p{
    color: gray;
}
h3{
    margin-top: 10px;
}
</style>