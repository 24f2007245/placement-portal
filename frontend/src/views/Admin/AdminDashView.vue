<script setup>
import { RouterLink } from 'vue-router';
import LogedinNav from '@/components/LogedinNav.vue';
import SideBar from '@/components/SideColumn.vue';

import Footer from '@/components/Footer.vue';
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
                <RouterLink to="/admin/past_drives" class="nav_ele">Past Drives</RouterLink>
            </div>
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
</style>