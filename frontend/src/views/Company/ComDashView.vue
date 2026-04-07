<script setup>
import Footer from '@/components/Footer.vue';
import LogedinNav from '@/components/LogedinNav.vue';
import Welcome from '@/components/SideColumn.vue';


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
</style>