
<template>
    <HomeNav/>
    <div id="reg-de">
        
        <h1>Login&emsp;</h1>
            <form method="POST" @submit.prevent="submitForm">
                <label for="email">EMAIL ID</label><br>
                <input type="email" name="email" id="email" v-model="formData.email" placeholder="example@zxy.com" required><br>

                <label for="password">PASSWARD</label><br>
                <input type="password" name="password" id="password" v-model="formData.password" placeholder="passoword" required><br><br>

                <button type="submit" class="bld">login</button><br><br>
                <p>{{ message }}</p>
                
                <!-- <router-link to="/login">or login here</router-link> -->
            </form>

    </div>
    <Footer/>
    
</template>

<script setup>
// import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'
import HomeNav from '@/components/HomeNav.vue'
import Footer from '@/components/Footer.vue'

const formData = reactive({
    email: 'admin@admin.com',
    password: ''
})

const message = ref('')


async function submitForm(){
    //console.log(formData)
    const response= await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })

    const data=await response.json()
    
    if(!response.ok){
        console.log('okvgytgvtde')
        message.value='ERROR HAPPENS: '+ data.message
    }else{
        
        localStorage.setItem('token', data.access_token)
        localStorage.setItem('email',data.email)
        localStorage.setItem('role',data.role)
        localStorage.setItem('user_name',data.user_name)
        localStorage.setItem('user_id',data.user_id)
        message.value="login successful Redirecting..."
        
        if (data.role=='student'){
        window.location.href='/student'
        }
        if(data.role=='admin'){
            window.location.href='/admin'
        }
        if(data.role=='company'){
            window.location.href='/company'
        }
        
    }

}



</script>

<style scoped>
#reg-de{
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    padding: 100px;

    /* align-items: center; */
}
h1{
    /* font-size:larger; */
    color: #2980b9;
}
input{
    width: 300px;
    line-height: 30px;
    margin: 1px;
}


@media(max-width:770px){
    #reg-de{
        display: block;
        padding: 30px;
    }
    input{
        width: 250px;
    }
}

</style>