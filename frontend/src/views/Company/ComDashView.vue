<script setup>
import { RouterLink,RouterView } from 'vue-router';
import { ref,onMounted} from 'vue';
import axios from 'axios';

import Footer from '@/components/Footer.vue';
import LogedinNav from '@/components/LogedinNav.vue';
import Welcome from '@/components/SideColumn.vue';


const stats = ref({
    total_drives: 0,
    total_applicants: 0,
    drives: 0,
})

async function fetchDashboardStats() {
    const token = localStorage.getItem('token')
    if (!token) {
        localStorage.clear()
        window.location.href = '/login'
        return
    }

    try {
        const response = await axios.get('http://127.0.0.1:5000/company/dashboard_stats', {
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
    <LogedinNav />
    <div id="full_con">
        <Welcome />
        <div id="rest_con">
            <div id="nav_link">
                <RouterLink to="/company/view_drives" class="nav_element">view_drives</RouterLink>
                <RouterLink to="/company/create_drives" class="nav_element">create_drives</RouterLink>
                <RouterLink to="/company/shortlisted_students" class="nav_element">shortlisted_students</RouterLink>
            </div>
            <div id="flex_box">
                <div class="box"><p>Total Drives</p><h3>{{ stats.total_drives }}</h3></div>
                <div class="box"><p>Total Applicants</p><h3>{{ stats.total_applicants }}</h3></div>
                <!-- <div class="box"><p>Drives</p><h3>{{ stats.drives }}</h3></div> -->
            </div>
            <router-view />
            <br><br><br>
            <div class="note">
                <h4>Note:</h4>
                <p>Any user access with role <code>company</code> can create drives but still drives are in pending
                    status until institute approves it.</p>
                
                    <p>Approved Drives are those drives which get approved by the admin.</p>
                    <p>Awaiting Dives are marked as pending status, students will see only after approved.</p>
                
            </div>
            <Footer/>
        </div>
    </div>
    <!-- <hr> -->



</template>

<style scoped>
#full_con {
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

#rest_con {
    flex: 1;
    min-width: 0;
    margin-top: 30px;
    padding: 10px;
}

@media(max-width:770px) {
    #full_con {
        display: block;
        padding: 10px;
    }

    #rest_con {
        margin-top: 10px;
        padding: 10;
    }

    #nav_link {
        flex-wrap: wrap;
    }

    /* #rest_con{
        margin-top: 10px;
    } */
}

.nav_element {
    color: #2980b9;
}

#nav_link {
    display: flex;
    gap: 10px;
}
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
    color: #2980b9;
    justify-content: center;
    background:linear-gradient(45deg,#f5f5f5, forestgreen);
}
</style>