<script setup>

import axios from 'axios'
import { ref, onMounted } from 'vue'


const rsusers = ref([])
const fetchStudent = async () => {

    try {
        const res = await axios.get(
            'http://127.0.0.1:5000/admin/registered_students',
            {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                }
            }
        )

        rsusers.value = res.data
    } catch (err) {
        console.log(err)
    }
}


onMounted(() => {
    fetchStudent()
})
</script>
<template>
    <div id="registered_students">
                <h1>Registered Students</h1><br>
                <table>
                    <thead><tr>
                        <th>Student ID</th>
                        <th>Student Name</th>
                        <th>Student Email</th>
                        <th>Blacklist</th>
                        <th>Remove</th>
                    </tr></thead>

                    <tbody><tr v-for="student in rsusers" :key="student.user_id">
                        <td>{{ student.user_id }}</td>
                        <td>{{ student.user_name }}</td>
                        <td>{{ student.user_email }}</td>
                        <td ><button class="dngr" @click="blackLIst(student.user_id)">blacklist</button></td>
                        <td><button class="dngr"> remove</button></td>
                    </tr></tbody>
                </table>
            </div>
</template>

<style scoped>
table{
    border-collapse: collapse;
    color: gray;
 }
 td{
    color: gray;
    padding: 5px;
 }
 th{
    padding: 5px;
 }

 #registered_company{
    margin-top: 30px;
 }
 #dngr{
    color: red;
 }</style>