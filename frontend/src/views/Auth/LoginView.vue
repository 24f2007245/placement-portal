
<template>
    <HomeNav/>
    <br><br><br><br>
    <div id="reg-de">
        
        <h5>Login&emsp;</h5>
            <form method="POST" @submit.prevent="submitForm">
                <label for="email">Enter Your Email Address:</label>
                <input type="email" name="email" id="email" v-model="formData.email" placeholder="example@zxy.com" required><br>

                <label for="password">Enter Your Password:</label>
                <input type="password" name="password" id="password" v-model="formData.password" placeholder="passoword" required><br>

                <button type="submit">login</button><br><br>
                <p>{{ message }}</p>
                
                <!-- <router-link to="/login">or login here</router-link> -->
            </form>

    </div>
    
</template>

<script setup>
import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'
import HomeNav from '@/components/HomeNav.vue'

const formData = reactive({
    email: 'pappu@gmail.com',
    password: 'kundan'
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
    
    console.log("data: "+data)
    if(!response.ok){
        console.log('okvgytgvtde')
        message.value='ERROR HAPPENS: '+ data.message
    }else{
        
        localStorage.setItem('token', data.access_token)
        localStorage.setItem('email',data.email)
        localStorage.setItem('role',data.role)
        message.value="login successful Redirecting..."
        
        if (data.role=='student'){
        window.location.href='/student/dash'
        }
        if(data.role=='admin'){
            window.location.href='/admin/dash'
        }
        if(data.role=='company'){
            window.location.href='/company/dash'
        }
        
    }

}



</script>

<style scoped>
#reg-de{
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    padding: 20px;
    /* align-items: center; */
}
h5{
    font-size:larger;
    color: #2980b9;
}

</style>