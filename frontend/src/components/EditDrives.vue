<script setup>
import {ref, onMounted, watch} from 'vue'
import { useRoute,useRouter } from 'vue-router';
import axios from 'axios';
import api from '@/services/api';

const drives=ref({
    job_title: '',
    job_description: '',
    branch: '',
    cgpa: '',
    year:'',
    application_deadline: ''
})
const route=useRoute()
const router=useRouter()
const id=route.params.id


const token=localStorage.getItem('token')


async function fetchDrives(id){ 

    if (!token){
        
        window.location.href='/'
        return
    }

    try{
        const response=await api.get(`/drives/${id}`,{
        headers:{
            Authorization: `Bearer ${token}`
        }
    })
    drives.value=response.data

    }catch(err){
        console.error(err)
    }

}
async function updateDrives(id){ 

    if (!token){
        
        window.location.href='/'
        return
    }

    try{
        const response=await api.put(`/drives/${id}`,
        drives.value,
        {
        headers:{
            Authorization: `Bearer ${token}`
        }
    })
    drives.value=response.data

    }catch(err){
        console.error(err)
    }

}


onMounted(
    ()=>{
        fetchDrives(id)
    }
)

</script>

<template>

</template>

<style scoped>
</style>