
<template>
    <HomeNav/>
    <br><br><br><br>
    <div id="reg-de">
        
        <h5>Register&emsp;</h5>
            <form method="POST" @submit.prevent="register">
                <label for="name">Enter Your Full Name:</label>
                <input type="text" name="name" id="name" v-model="formData.name" placeholder="Chhotu Kumar" required><br>

                <label for="email">Enter Your Email Address:</label>
                <input type="email" name="email" id="email" v-model="formData.email" placeholder="example@zxy.com" required><br>

                <label for="password">Enter Your Password:</label>
                <input type="password" name="password" id="password" v-model="formData.password" placeholder="passoword" required><br>

                <label for="role">select role: </label>
                <select name="role" id="role" v-model="formData.role">
                    <option value="">choose role</option>
                    <option value="student">student</option>
                    <option value="company">company</option>
                </select>
                <!-- <label for="role">Role:</label>
                <input type="text" name="role" id="role" v-model="formData.role" placeholder="student" required><br> -->

                <button type="submit">Register</button><br><br>
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
    name: 'kundan',
    email: '',
    password: 'kundan',
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
    padding: 20px;
    /* align-items: center; */
}
h5{
    font-size:larger;
    color: #2980b9;
}
select{
    padding: 3px;
    background-color: #2980b9;
    color: white;
}

</style>