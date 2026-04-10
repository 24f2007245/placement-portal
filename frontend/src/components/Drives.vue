<script setup>

// importing ________________________________
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const message = ref('')
const drives = ref([])
const approved_drive=ref([])
const awaiting_drive=ref([])
const applied_drive_ids = ref([])
const role=localStorage.getItem('role')
const router=useRouter()
const route=useRoute()


// functions____________________________________________




function subDescription(des){
    if (des.length > 50){
        return des.slice(0,50)+"...";
    }
    else{
        return des
    }
}

// getting application of students___________________
// get request

async function fetchStudentApplications() {
    const token =localStorage.getItem('token')
    if(!token || !isStudent()) {
        return
    }

    try {
        const response = await axios.get('http://127.0.0.1:5000/student/applications', {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })

        applied_drive_ids.value =response.data.map(app => app.drive_id)
    }catch (error) {
        applied_drive_ids.value =[]
    }
}

// END of get request___________________


// chhota  function
function isApplied(drive_id){

    return applied_drive_ids.value.includes(drive_id)
}

// chhotafunction
function isAdmin(){
    return role === 'admin'
}


//chhota function
function isStudent(){
    return role === 'student'
}
  
// fetching ______________________________
// get request

const fetchDrives = async ()=>{
    const token = localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try{
        const response =await axios.get(
            'http://127.0.0.1:5000/drives',
            {
                params:{
                    search: (route.query.search || '').toString()
                },
                headers:{
                    Authorization: `Bearer ${token}`
                }
            }
        )

        drives.value = response.data
        approved_drive.value= []
        awaiting_drive.value= []
        for(let drive of drives.value){
            if(drive.status===1){
                approved_drive.value.push(drive)
            }else{
                awaiting_drive.value.push(drive)
            }
        }
        console.log(approved_drive)
        console.log(awaiting_drive)
    }catch(error) {
        console.error(error)
        if (error.response?.status === 401){
            localStorage.clear()
            window.location.href= '/login'
            return}
        message.value = "Failed to load drives"
    }
}

// END of fetchDrives with get ________________________________


function driveDetail(drive_id){
    router.push(`/drive/${drive_id}`)
}



// approving_____________________________________________________
// patch request

async function approveDrive(drive_id){
    const token = localStorage.getItem('token')
    if(!token){
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

// END approving with patch request____________________________________


// deleting___________________________
// delete request

async function removeDrive(drive_id) {
    const token= localStorage.getItem('token')
    if(!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try{
        const response =await axios.delete(
            `http://127.0.0.1:5000/admin/remove_drive/${drive_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        message.value ='drive removed successfully'
        fetchDrives()
    }catch(error){
        if (error.response?.status === 401) {
            localStorage.clear()
            window.location.href= '/login'
            return
        }
        message.value= 'failed to remove drive'
    }
}

// END delete request________________________________________________



// posting_______________________________
// post request

async function applyDrive(drive_id){
    const token= localStorage.getItem('token')
    if(!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try{
        const response= await axios.post(
            `http://127.0.0.1:5000/apply_drive/${drive_id}`,
            {},
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        message.value = response.data?.message || 'applied successfully'
        applied_drive_ids.value.push(drive_id)
    } catch (error) {
        if (error.response?.status === 401 ){
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        if (error.response?.status === 409){
            message.value = 'already applied'
            if (!isApplied(drive_id)){
                applied_drive_ids.value.push(drive_id)
            }
            return
        }
        message.value = 'failed to apply, if you have not updated the profile, please update first upload resume...'
    }
}

// END post request_____________________________________

onMounted(() => {
    fetchDrives()
    fetchStudentApplications()
})

watch(
    () => route.query.search,
    () => {
        fetchDrives()
    }
)
</script>
<template>
            <div v-if="message" style="padding: 10px; background-color: #f5f5f5; color: cadetblue; text-decoration: overline;"><p>{{ message }}</p></div>
    
            <div id="awaiting_drive" v-if="isAdmin()">
                <p style="color: chocolate;">Total Number Of Awaiting Drives is {{ awaiting_drive.length }}</p>
                <h1>Awaiting Drives</h1><br>
                <div class="table">
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
                        <td ><button class="dngr" @click="removeDrive(drive.drive_id)">remove</button></td>
                        
                        
                    </tr>
                    </tbody>
                    </table>
                    <p v-else>no records</p>
                </div>
            </div>
            <br>
            <div id="approved_drive">
                <h1>Ongoing Drives</h1><br>
                <p style="color: chocolate;">Total Number Of Ongoing Drives is {{ approved_drive.length }}</p>
                <div class="table">
                    <table v-if="approved_drive.length>0">
                    <thead>
                        <tr>
                        <th>Drive ID</th>
                        <th>Company ID</th>
                        <th>Job Title</th>
                        <th>Description</th>
                        <th>Branch</th>
                        <th>CGPA</th>
                        <th>Year</th>
                        <th>Deadline</th>
                        <th>Details</th>
                        <template v-if="isAdmin()">
                            
                            <th >Remove</th>
                        </template>
                        <template v-else>
                            <th v-if="isStudent()">Apply</th>
                        </template>
                        
                    </tr>
                    </thead>

                    <tbody>
                        <tr v-for="drive in approved_drive" :key="drive.drive_id">
                        <td>{{ drive.drive_id }}</td>
                        <td>{{ drive.company_id }}</td>
                        <td>{{ drive.job_title }}</td>
                        <td>{{ subDescription(drive.job_description) }}</td>
                        <td>{{ drive.branch }}</td>
                        <td>{{ drive.cgpa }}</td>
                        <td>{{ drive.year }}</td>
                        <td>{{ drive.application_deadline }}</td>
                        <td><button @click="driveDetail(drive.drive_id)">details</button></td>

                        <template v-if="isAdmin()">
                            
                            <td ><button class="dngr" @click="removeDrive(drive.drive_id)">remove</button></td>
                        </template>
                        <template v-else-if="isStudent()">
                            <td>
                                <button @click="applyDrive(drive.drive_id)" :disabled="isApplied(drive.drive_id)" :class="{ 'faded_btn': isApplied(drive.drive_id) }">
                                    {{ isApplied(drive.drive_id) ? 'applied' : 'apply' }}
                                </button>
                            </td>
                        </template>
                        
                    </tr>
                    </tbody>
                    </table>
                    <p v-else>no records</p>
                </div>
                
            </div>
</template>
<style scoped>

@media(max-width:770px){
    #awaiting_drive{
        padding: 20px;
    }
    #approved_drive{
        padding: 20px;
    }
}

.faded_btn{
    opacity: 0.5;
    cursor: not-allowed;
}



</style>