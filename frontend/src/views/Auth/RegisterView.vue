
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
                <div v-if="formData.role==='company'" style="max-width: 310px;">
                    <!-- <p>pay one time registration fee of RS 7 for a company registration</p>
                    <button type="button" class="rzp-button1" @click="handlePay">Pay</button><br><br>
                    <p v-if="paymentSuccess" style="color:green">Payment verified ✓</p>
                    <p v-else style="color:#a33">Payment not completed</p>
                    <p>
                        async function handlePay(){
                        message.value = ''
                        try{
                            // ensure checkout script
                            await loadScript('https://checkout.razorpay.com/v1/checkout.js')

                            // amount in paise (7 INR)
                            const amount = 700

                            const resp = await api.post('/api/create-order', { amount: amount, currency: 'INR' })
                            const data = resp.data || resp
                            const orderId = data.order_id || data.orderId || data.id
                            if(!orderId){
                                message.value = 'Failed to create order'
                                return
                            }

                            const options = {
                                key: import.meta.env.VITE_RAZORPAY_KEY_ID,
                                amount: data.amount || amount,
                                currency: data.currency || 'INR',
                                name: 'Placement Portal',
                                description: 'Company registration fee',
                                order_id: orderId,
                                handler: async function (response){
                                    try{
                                        await api.post('/api/verify-payment', {
                                            razorpay_order_id: response.razorpay_order_id,
                                            razorpay_payment_id: response.razorpay_payment_id,
                                            razorpay_signature: response.razorpay_signature
                                        })
                                        paymentSuccess.value = true
                                        message.value = 'Payment successful and verified'
                                    }catch(err){
                                        paymentSuccess.value = false
                                        message.value = 'Payment verification failed'
                                    }
                                },
                                modal: {
                                    ondismiss: function(){
                                        message.value = 'Payment cancelled'
                                    }
                                }
                            }

                            const rzp = new window.Razorpay(options)
                            rzp.open()
                            rzp.on('payment.failed', function (response){
                                message.value = 'Payment failed: ' + (response.error && response.error.description ? response.error.description : '')
                            })

                        }catch(e){
                            console.error(e)
                            message.value = 'Payment initialization failed'
                        }
                    }

                    </p> -->
                    
                    <p class="note">Note: this platform does not show its true nature it is not a real placement portal and not managed by anyone it is just one indivisual demo project. Do transaction with your own risks.</p>
                </div>

                <button type="submit" class="bld">Register</button><br><br>
                <p>{{ message }}</p>
                <!-- <router-link to="/login">or login here</router-link> -->
            </form>

    </div>
    
    <Footer/>
    
</template>

<script setup>
// import { RouterLink } from 'vue-router'
import {ref, reactive} from 'vue'
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
    message.value = ''

    try {

        const response = await api.post('/register', {
            ...formData
        })

        message.value = 'Registration Successful'

    } catch(error) {

        message.value =
            'Registration Failed: ' +
            (error.response?.data?.message || error.message)
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
        padding: 25px;
        padding-top: 50px;
        padding-bottom: 50px;
        /* align-items: center; */
        /* place-items: center; */
    }
    input{
        width: 250px;
        
    }
}
</style>