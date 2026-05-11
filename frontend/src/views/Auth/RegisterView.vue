
<template>
    <HomeNav/>
    <div id="reg-de">
        
        <h1>Register&emsp;</h1>
            <form method="POST" @submit.prevent="register">
                <label for="name">Enter Your Full Name:</label><br>
                <input type="text" name="name" id="name" v-model="formData.name" placeholder="Chhotu Kumar" required><br>

                <label for="email">Enter Your Email Address:</label><br>
                <input type="email" name="email" id="email" v-model="formData.email" placeholder="example@zxy.com" required><br>

                <label for="password">Enter Your Password:</label><br>
                <input type="password" name="password" id="password" v-model="formData.password" placeholder="passoword" required><br><br>

                <label for="role">Select Role: </label>
                <select name="role" id="role" v-model="formData.role">
                    <option value="">choose role</option>
                    <option value="student" disabled>student</option>
                    <option value="company">company</option>
                </select><br><br>
                <!-- <label for="role">Role:</label>
                <input type="text" name="role" id="role" v-model="formData.role" placeholder="student" required><br> -->

                <button type="submit" class="bld">Register</button><br><br>
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
import HowToRegister from '@/components/HowToRegister.vue'
import Footer from '@/components/Footer.vue'
import api from '@/services/api'

const formData = reactive({
    name: '',
    email: '',
    password: '',
    role: ''
})

const message = ref('')

console.log(formData)
async function register(){
    try {
        const response = await api.post('/register', formData)
        const data = response.data
        console.log(data)
        message.value='Registration Successful, note:company need institute approval, kindly wait till'
        // window.location.href ='/login'
    } catch(error) {
        message.value='Registration Failed: '+(error.response?.data?.message || error.message)
    }

    }



</script>

<style scoped>
#reg-de{
    background-color: white;
    display: flex;
    justify-content: center;
    /* place-items: center; */
    padding: 100px;
    color: #3b7ca6;
    
    
    /* align-items: center; */
    /* align-items: center; */
}
h1{
    /* font-size:larger; */
    font-size: 2.5rem;
    color: #3b7ca6;
    padding-bottom: 30px;
}
select{
    padding: 3px;
    background-color: #3b7ca6;
    color: white;
    border: 1px solid #3b7ca6;
    width: 150px;
    height: 30px;
}

input{
    margin: 1px;
    /* padding: 0; */
    width: 300px;
    line-height: 30px;
    /* border: none; */
}


@media(max-width:600px){
    #reg-de{
        display: block;
        justify-content: center;
        /* place-items: center; */
        padding: 30px;
        padding-top: 50px;
        padding-bottom: 50px;
    }
    input{
        width: 250px;
        
    }
}
</style>