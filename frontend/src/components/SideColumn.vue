<script setup>

// IMPORTS H_______________
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

// _____________________________END



// variables______________________


const user_email=(localStorage.getItem('email') || '').toUpperCase()
const user_role= localStorage.getItem('role')

const user_name=(localStorage.getItem('user_name') || '').toUpperCase()
const route=useRoute()
const router =useRouter()
const search =ref((route.query.search || '').toString())

//  ____________end




// FUNCTIONS________________


function applySearch() {
    const query= { ...route.query }
    if (search.value && search.value.trim() !== '') {
        query.search = search.value.trim();
    } else {
        delete query.search;
    }

    router.push({ path: route.path, query: query })
}

watch(
    () => route.query.search,
    (value) => {
        search.value = (value || '').toString()
    }
)
</script>
<template>
    <div id="main">
        <div id="div_search">
            <h1>Welcome {{ user_name }}</h1><h3>{{ user_email }}</h3>
            <!-- <label for="search"><h3>Search</h3></label> -->
            <span><input type="search" id="search" placeholder="search" v-model="search" @keyup.enter="applySearch"></span>
            <span><button type="submit" @click="applySearch">find</button></span>
        </div>



        <p v-if="user_role==='admin'" class="note">NOTE: <br>
            1.In the dashboard there are many section like drives, registered_company, registed_student; to search drives related things go into that section and then search with <code>drive_id,job_title,company_id ...</code>, for other section do the same <br>
        </p>
        <p v-if="user_role==='company'" class="note">NOTE: 
            <br>1.In the dashboard there are many section like drives; to search drives related things go into that section and then search with <code>drive_id,job_title,job_description</code>, for other section do the same <br>
            2.In some section you will not search facility, if you are trying to search but not working, don't get ...
        </p>
        <p v-if="user_role==='student'" class="note">NOTE: <br> 
            1.In the dashboard there are many section like drives, to search drives related things go into that section and then search with <code>drive_id,job_title, </code><code>job_description,company_id </code><code>,cgpa,year,deadline.</code><br>
            2.In some section you will not have search facility, if you are trying to search but not working, don't get ...
        </p>

 
        

    </div>

</template>

<style scoped>
#main{
    /* background-color: #f5f5f5; */
    width: 280px;
    max-width: 100%;
    flex-shrink: 0;
    /* height: 100%; */
    color: #2980B9;
    margin: 30px;
    display: flex;
    flex-direction: column;
    /* position:static; */
}

button{
        width: 60px;
    }
    


@media(max-width:760px){
    #main{
        width:100%;
        margin:10px;
        
    }
    #div_search{
        padding-top: 20px;
        padding-bottom: 20px;
    }
    
}
input{
    padding: 4px;
}
button{
    margin: 3px;
    border: 2px solid cadetblue;
    font-weight: bold;
    /* text-decoration: underline; */
}

</style>