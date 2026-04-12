<script setup>
import Footer from '@/components/Footer.vue';
import LogedinNav from '@/components/LogedinNav.vue'
import Welcome from '@/components/SideColumn.vue'
// import Drives from '@/components/Drives.vue';
// import Drives from '@/components/drives.vue';


</script>

<template>
    <LogedinNav/>
    <div id="full_con">
        <Welcome/>
        
        <div id="rest_con">
            <!-- <h1>student's dashboard</h1> -->
             <div class="nav">
                <RouterLink to="/student/drives" class="nav_ele">Placements_Drives</RouterLink>
                <RouterLink to="/student/profile" class="nav_ele">Student_Profile</RouterLink>
                <RouterLink to="/student/applications" class="nav_ele">My_Applications</RouterLink>
                <RouterLink to="/student/past_drives" class="nav_ele">Past Drives</RouterLink>
             </div>
            <router-view/>
            <Footer/>
        </div>
    </div>
    
</template>

<style scoped>
h1{
    padding: 10px;
}
#full_con{
    display: flex;
}
.nav{
    padding: 10px;
    padding-top: 30px;
}
@media(max-width:770px){
    #full_con{
        display: block;
    }
}

</style>

