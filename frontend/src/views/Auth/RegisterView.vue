
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
                    <option value="student">student</option>
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

const formData = reactive({
    name: 'kundan',
    email: '',
    password: '',
    role: 'student'
})

const message = ref('')

console.log(formData)
async function register(){
    const response= await fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
        })
        console.log(response)

        const data= await response.json()
        console.log(data)
        if (!response.ok){
            return message.value='Registration Failed: '+data.message
        }else{
            message.value='Registration Successful'
            window.location.href ='/login'
        }

    }



</script>

<style scoped>
#reg-de{
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    padding: 70px;
    /* align-items: center; */
    /* align-items: center; */
}
h1{
    /* font-size:larger; */
    color: #2980b9;
}
select{
    padding: 3px;
    background-color: white;
    color: #2980b9;
    border: 1px solid #2980b9;
    
}
@media(max-width:770px){
    #reg-de{
        display: block;
        padding: 30px;
    }
}
input{
    margin: 1px;
    /* padding: 0; */
    width: 300px;
    line-height: 30px;
    /* border: none; */
}
select{
    width: 150px;
    height: 30px;
}

</style>