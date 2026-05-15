
<template>
    <HomeNav/>
    <div id="reg-de">
        
        <div class="flex">
            <h1>Login&emsp;</h1>
            <div>
                <form method="POST" @submit.prevent="submitForm">
                <label for="email">EMAIL ID</label><br>
                <input type="email" name="email" id="email" v-model="formData.email" placeholder="example@zxy.com" required><br>

                <label for="password">PASSWARD</label><br>
                <input type="password" name="password" id="password" v-model="formData.password" placeholder="passoword" required><br><br>

                <button type="submit" class="bld">login</button><br><br>
                <p>{{ message }}</p><br>
                <div id="auth">
                    <p>or</p><br>
                    <div id="googleSignInDiv">sign in with google</div>
                
                </div> 
                
                <!-- <router-link to="/login">or login here</router-link> -->
            </form>
            </div>
        </div>
        
    </div>
    
    <Footer/>
    
</template>

<script setup>
// import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'
import HomeNav from '@/components/HomeNav.vue'
import Footer from '@/components/Footer.vue'
import api from '@/services/api'

const formData = reactive({
    email: 'admin@admin.com',
    password: ''
})

const message = ref('')


async function submitForm(){
    message.value = ''
    //console.log(formData)
    const response = await api.post('/login', formData)

    try {
        const data = response.data
        
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
    } catch (error) {
        console.log('Error during login')
        message.value='ERROR HAPPENS: '+ (error.response?.data?.message || error.message)
    }

}


// auth -------------------------------------------------------------------

const handleCredentialResponse = async (response) => {
  const token = response.credential;

  try {
    const res = await api.post("/auth/google", { token });
    const data = res.data;
    // console.log(data)

    // store your JWT
    localStorage.setItem('token', data.access_token)
    localStorage.setItem('email',data.email)
    localStorage.setItem('role',data.role)
    localStorage.setItem('user_name',data.user_name)
    localStorage.setItem('user_id',data.user_id)
    message.value=data.message
    
    if (data.role=='student'){
    window.location.href='/student'
    }
    if(data.role=='admin'){
        window.location.href='/admin'
    }
    if(data.role=='company'){
        window.location.href='/company'
    }

    console.log("Login success");
  } catch (err) {
    console.error("Login failed", err);
    message.value='ERROR HAPPENS: '+ (err.response?.data?.message || err.message)
  }
};

onMounted(() => {
  /* global google */
  if (!window.google) {
    console.error("Google script not loaded");
    return;
  }

  window.google.accounts.id.initialize({
    client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
    callback: handleCredentialResponse
  });

  window.google.accounts.id.renderButton(
    document.getElementById("googleSignInDiv"),
    {
      theme: "outline",
      size: "large"
    }
  );
});

// end auth---------------------------------------------------------

</script>

<style scoped>
#reg-de{
    background-color: white;
    display: grid;
    justify-content: center;
    place-items: center;
    padding: 100px;
    color: #3b7ca6;

    /* align-items: center; */
}
h1{
    /* font-size:larger; */
    color: #3b7ca6;
    font-size: 2.5rem;
    padding-bottom: 30px;
}
input{
    width: 300px;
    line-height: 30px;
    margin: 1px;
}



#auth{
    /* width: 250px; */
    display: grid;
    place-items: center;
    padding-left: auto;
}

#googleSignInDiv{
    width: 300px;
    border: 1px solid #29b;
    color: gray;
    /* padding: 10px; */
}

.flex{
    display: flex;
}


@media(max-width:600px){
    .flex{
        display: block;
        
    }
    input{
        width: 250px;
    }
    #googleSignInDiv{
    width: 250px;
    
    }
    #reg-de{
        padding: 30px;
        padding-top: 50px;
        padding-bottom: 50px;
    }
}

</style>