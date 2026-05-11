
<script setup>

// importing ___________
import {ref} from 'vue'
import axios from 'axios'
import { useRoute,useRouter } from 'vue-router'
import LogedinNav from './LogedinNav.vue'
import api from '@/services/api'

const route=useRoute()
const router=useRouter()

const company=ref({
    company_id: '',
    hr_no: '',
    company_description: '',
    website: '',
})

async function companyDetails(company_id){
    const token=localStorage.getItem('token')
    
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await api.get(`/company_profile/${company_id}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        
        if (response.data?.company_id !== undefined) {
            company.value = response.data
            
        } else {
            message.value = response.data?.message
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

companyDetails(route.params.id)


</script>

<template>
    <LogedinNav/>
    <div id="content">
        <button @click="router.back()">Back</button>
        <p>Company Id: </p><p>{{ company.company_id }}</p>
        <p>Description: </p><p>{{ company.company_description }}</p>
        <p>HR No: </p><p>{{ company.hr_no }}</p>
        <p>Company's Official Website: </p><p>{{ company.website }}</p>

    </div>

</template>

<style scoped>
#content{
    padding: 20px;
    background:#f5f5f5 ;
    
    /* padding-right: 50%; */
}
p{
    padding: 3px;
    color: gray;
}
</style>