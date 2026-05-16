<script setup>

import { ref, onMounted } from 'vue'
import api from '@/services/api'
import LoadingSpinner from '@/components/LoadingSpinner.vue'


const rsusers= ref([])
const message = ref('')
const isLoading = ref(false)
const minLoadingMs = 400

function finishLoading(startTime) {
    const elapsed = Date.now() - startTime
    const remaining = Math.max(0, minLoadingMs - elapsed)
    setTimeout(() => {
        isLoading.value = false
    }, remaining)
}
const fetchStudent = async () => {
    const startTime = Date.now()

    try{
        isLoading.value = true
        message.value = ' '
        const res = await api.get(
            '/admin/registered_students',
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            }
        )

        rsusers.value = res.data
    }catch (err) {
        console.log(err)
    } finally {
        finishLoading(startTime)
    }
}

// function blackList(){
//     return
// }

async function removeStudent(student_id) {
    const token = localStorage.getItem('token')
    if (!token){
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try{
        message.value = ' '
        const response = await api.delete(
            `/admin/remove_student/${student_id}`,
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )
        message.value = response.data?.message || 'student removed successfully'
        fetchStudent()
    } catch(err){
        message.value = err.response?.data?.message || 'failed to remove student'
    }
}


onMounted(() =>{
    fetchStudent()
})
</script>
<template>
    <div id="registered_students">
        <p style="color: chocolate;">Total Number Of Resgistered users is {{ rsusers.length }}</p>
                <p v-if="message">{{ message }}</p>
                <h1>Registered Students</h1><br>
                <div v-if="isLoading" class="inline-loader">
                    <LoadingSpinner label="Loading" />
                </div>
                <div class="table">
                    <table>
                    <thead><tr>
                        <th>Student ID</th>
                        <th>Student Name</th>
                        <th>Student Email</th>
                        <!-- <th>Blacklist</th> -->
                        <th>Remove</th>
                    </tr></thead>

                    <tbody><tr v-for="student in rsusers" :key="student.user_id">
                        <td>{{ student.user_id }}</td>
                        <td>{{ student.user_name }}</td>
                        <td>{{ student.user_email }}</td>
                        <!-- <td ><button class="dngr" @click="blackList(student.user_id)">blacklist</button></td> -->
                        <td><button class="dngr" @click="removeStudent(student.user_id)"> remove</button></td>
                    </tr></tbody>
                </table>
                </div>
            </div>
</template>

<style scoped>


 #registered_company{
    margin-top: 30px;
 }
 #dngr{
     color: red;
 }

.inline-loader{
     margin: 8px 0 12px;
}
</style>