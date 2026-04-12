<script setup>
import { RouterLink,RouterView } from 'vue-router';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import LogedinNav from '@/components/LogedinNav.vue';
import SideBar from '@/components/SideColumn.vue';

import Footer from '@/components/Footer.vue';

const message = ref('')
const stats = ref({
    total_students: 0,
    total_companies: 0,
    total_drives: 0,
})

async function fetchDashboardStats() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get('http://127.0.0.1:5000/admin/dashboard_stats', {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })

        stats.value = response.data
    } catch (error) {
        if (error.response?.status === 401 || error.response?.status === 422) {
            localStorage.clear()
            window.location.href = '/login'
            return
        }
        message.value = error.response?.data?.message || 'failed to load dashboard stats'
    }
}

onMounted(() => {
    fetchDashboardStats()
})


</script>

<template>
    
    <LogedinNav/>
    <div id="cnt">
        <SideBar/>
        <div id="content">
            <div id="content_nav">
                <RouterLink to="/admin/drives" class="nav_ele">drives</RouterLink>
                <RouterLink to="/admin/company_application" class="nav_ele">approve_company</RouterLink>
                <RouterLink to="/admin/registered_company" class="nav_ele">registered_company</RouterLink>
                <RouterLink to="/admin/registered_students" class="nav_ele">registered_students</RouterLink>
                <RouterLink to="/admin/student_applications" class="nav_ele">student_applications</RouterLink>
                <RouterLink to="/admin/hired_students" class="nav_ele">hired_students</RouterLink>
            </div>
            <p v-if="message">{{ message }}</p>
            <div id="flex_box">
                <div class="box"><p>Total Companies</p><h3>{{ stats.total_companies }}</h3></div>
                <div class="box"><p>Total Students</p><h3>{{ stats.total_students }}</h3></div>
                <div class="box"><p>Total Drives</p><h3>{{ stats.total_drives }}</h3></div>
            </div><br><br>
            <!-- <CountView/> -->
            <router-view />
            <!-- <Drives/>
            <CompanyApplication/> -->
            
<!-- <br> -->
            <Footer/>
            

        </div>

    
    </div>
 
</template>

<style scoped>
#cnt{
    display: flex;
    color: #2980b9;
}

@media(max-width:770px){
    #cnt{
        display: block;
        /* padding: 20px; */
    }
    
}

@media(max-width:500px){
   
    #flex_box{
        display: inline;
     }
}


#content_nav{
    margin-top: 20px;
    padding: 10px;
    justify-content: space-between;
    
}

#content{
    width: 100%;
}

  /* RouterLink{
    text-decoration: none;
    padding: 10px;
  } */
#flex_box{
    display: flex;
}
.box{
    /* display: inline; */
    padding: 30px;
    /* border: 2px solid #2980b9; */
    /* width: 60px; */
    margin-left:10px ;
    margin-top: 20px;
    align-items: center;
    color: #f5f5f5;
    justify-content: center;
    background:linear-gradient(60deg,#f5f5f5, forestgreen);
}

</style>
