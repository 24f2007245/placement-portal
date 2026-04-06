<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const message = ref('')
const drives = ref([])
const approved_drive=ref([])
const awaiting_drive=ref([])
const role=localStorage.getItem('role')
const router=useRouter()

function subDescription(des){
    if (des.length > 50){
        return des.slice(0,50)+"...";
    }
    else{
        return des
    }
}

function isAdmin() {
    return role === 'admin'
  }
  

const fetchDrives = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get(
            'http://127.0.0.1:5000/drives',
            
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        drives.value = response.data
        approved_drive.value = []
        awaiting_drive.value = []
        for(let drive of drives.value){
            if(drive.status===1){
                approved_drive.value.push(drive)
            }else{
                awaiting_drive.value.push(drive)
            }
        }
    } catch (error) {
        console.error(error)
        if (error.response?.status === 401) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = "Failed to load drives"
    }
}

function driveDetail(drive_id){
    router.push(`/drive/${drive_id}`)
}

async function approveDrive(drive_id){
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }
    try{
        await axios.patch(`http://127.0.0.1:5000/approve_drive/${drive_id}`,
            {status:1},
            {
                headers:{
                    Authorization:`Bearer ${token}`
                }

            }
        )
        message.value='approve request captured successfully, refresh page '

    }catch(err){
        message.value=err
    }
}

onMounted(() => {
    fetchDrives()
})
</script>
<template>
    
            <div id="awaiting_drive" v-if="isAdmin()">
                <p style="color: chocolate;">Total Number Of Ongoing Drives is {{ approved_drive.length }}</p>
                <p style="color: chocolate;">Total Number Of Awaiting Drives is {{ awaiting_drive.length }}</p>

<div v-if="message" style="padding: 10px; background-color: #f5f5f5; color: cadetblue; text-decoration: overline;"><p >{{ message }}</p></div>
                <h1>Awaiting Drives</h1><br>
                <table v-if="awaiting_drive.length>0">
                <thead>
                    <tr>
                    <th>Drive ID</th>
                    <th>Company ID</th>
                    <th>Job Title</th>
                    <th>Description</th>
                    <!-- <th>Branch</th> -->
                    <!-- <th>Year</th> -->
                    <!-- <th>Deadline</th> -->
                    <th>Details</th>
                    
                    <th >Approve</th>
                    <th >Remove</th>
                    
                    
                </tr>
                </thead>

                <tbody>
                    <tr v-for="drive in awaiting_drive" :key="drive.drive_id">
                    <td>{{ drive.drive_id }}</td>
                    <td>{{ drive.company_id }}</td>
                    <td>{{ drive.job_title }}</td>
                    <td>{{ subDescription(drive.job_description) }}</td>
                    <!-- <td>{{ drive.branch }}</td> -->
                    <!-- <td>{{ drive.year }}</td> -->
                    <!-- <td>{{ drive.application_deadline }}</td> -->
                    <td><button @click="driveDetail(drive.drive_id)">details</button></td>

                    
                    <td ><button @click="approveDrive(drive.drive_id)">approve</button></td>
                    <td ><button class="dngr">remove</button></td>
                    
                    
                </tr>
                </tbody>
                </table>
                <p v-else>no records</p>
            </div>
            <br>
            <div id="approved_drive">
                <h1>Ongoing Drives</h1><br>
                <table v-if="approved_drive.length>0">
                <thead>
                    <tr>
                    <th>Drive ID</th>
                    <th>Company ID</th>
                    <th>Job Title</th>
                    <th>Description</th>
                    <!-- <th>Branch</th> -->
                    <!-- <th>Year</th> -->
                    <!-- <th>Deadline</th> -->
                    <th>Details</th>
                    <template v-if="isAdmin()">
                        
                        <th >Remove</th>
                    </template>
                    <template v-else>
                        <th>Apply</th>
                    </template>
                    
                </tr>
                </thead>

                <tbody>
                    <tr v-for="dri in approved_drive" :key="dri.drive_id">
                    <td>{{ dri.drive_id }}</td>
                    <td>{{ dri.company_id }}</td>
                    <td>{{ dri.job_title }}</td>
                    <td>{{ subDescription(dri.job_description) }}</td>
                    <!-- <td>{{ drive.branch }}</td> -->
                    <!-- <td>{{ drive.year }}</td> -->
                    <!-- <td>{{ drive.application_deadline }}</td> -->
                    <td><button @click="driveDetail(dri.drive_id)">details</button></td>

                    <template v-if="isAdmin()">
                        
                        <td ><button class="dngr">remove</button></td>
                    </template>
                    <template v-else>
                        <th><button>apply</button></th>
                    </template>
                    
                </tr>
                </tbody>
                </table>
                <p v-else>no records</p>
            </div>
</template>
<style scoped>
#approved_drives{
    color: #2980B9;
    /* overflow: hidden; */
    /* margin-top: 30px;
    margin-right: 20px; */
}
@media(max-width:770px){
    #awaiting_drive{
        padding: 20px;
    }
    #approved_drive{
        padding: 20px;
    }
}


</style>