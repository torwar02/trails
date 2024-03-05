<template>
  <v-card class="mx-auto dialog">
    <v-btn class="close-btn" @click="closeDialog">
      <v-icon name="fa-angle-left" />
    </v-btn>
    <div class="title">
      <div v-if="showLoginInChildren">
        <div>Welcome back.</div>
        <div>Log in and start exploring</div>
      </div>
      <div v-else>
        <div>Sign up today to start planning</div>
        <div>your next adventure</div>
      </div>
    </div>
    <v-container>
      <div v-if="showLoginInChildren">
        <v-text-field
          v-model="loginInfo.email"
          color="primary"
          label="Email Address"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="loginInfo.password"
          color="primary"
          label="Password"
          placeholder="Enter your password"
          variant="underlined"
          type="password"
        ></v-text-field>
      </div>
      <!-- sign up -->
      <div v-else>
        <v-text-field
          v-model="signupInfo.firstname"
          color="primary"
          label="First name"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="signupInfo.lastname"
          color="primary"
          label="Last name"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="signupInfo.email"
          color="primary"
          label="Email Address"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="signupInfo.password"
          color="primary"
          label="Password"
          placeholder="Enter your password"
          variant="underlined"
          type="password"
        ></v-text-field>
      </div>
    </v-container>
    <div class="footer">
      <div v-if="showLoginInChildren">
        <span>Don't have an account?</span>
        <a @click="showLoginInChildren = false">Sign up for free</a>
      </div>
      <div v-else>
        <span>Already have an account?</span>
        <a @click="showLoginInChildren = true">Log in</a>
      </div>
    </div>
    <span v-if="errorMsg" class="errorMessage">{{ errorMsg }}</span>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="success"
        @click.prevent="showLoginInChildren ? loginHandler() : singupHandler()"
      >
        <span v-if="showLoginInChildren">Log in</span>
        <span v-else>Complete Registration</span>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { ref, watch, defineEmits } from 'vue'
import requests from '../../services/requests'
import { user } from '../../services/apis'

const errorMsg = ref('')
const props = defineProps({
  showLogin: Boolean
})
const showLoginInChildren = ref(props.showLogin)
const emits = defineEmits(['closeDialog', 'loginSuccess'])
const closeDialog = () => {
  emits('closeDialog')
}
const loginInfo = ref({
  email: '',
  password: ''
})
const signupInfo = ref({
  firstname: '',
  lastname: '',
  email: '',
  password: ''
})
const initInfo = (obj) => {
  for (const key of Object.keys(obj.value)) {
    obj.value[key] = ''
  }
}
const loginHandler = () => {
  requests
    .post(user.login, loginInfo.value)
    .then((res) => {
      const { data, status, message } = res.data
      if (status === 'SUCCESS') {
        emits('loginSuccess', data[0])
      } else {
        throw { errmsg: message }
      }
    })
    .catch((err) => {
      initInfo(loginInfo)
      errorMsg.value = err.errmsg
        ? `${err.errmsg}, Please try again!`
        : 'Something went wrong, Please try again!'
    })
}
const singupHandler = () => {
  requests
    .post(user.signup, signupInfo.value)
    .then((res) => {
      const { data, status, message } = res.data
      if (status === 'SUCCESS') {
        showLoginInChildren.value = true
        loginInfo.value.email = data.email
      } else {
        throw { errmsg: message }
      }
    })
    .catch((err) => {
      initInfo(signupInfo)
      errorMsg.value = err.errmsg
        ? `${err.errmsg}, Please try again!`
        : 'Something went wrong, Please try again!'
    })
}

watch(
  [loginInfo, signupInfo],
  () => {
    errorMsg.value = ''
  },
  { deep: true }
)
</script>

<style lang="less" scoped>
.dialog {
  position: relative;
  width: 600px;
  .close-btn {
    position: absolute;
    width: 64px;
    height: 32px;
    left: 0;
    top: 12px;
  }
  .title {
    font-size: 32px;
    font-weight: bold;
    line-height: 1.1;
    display: flex;
    text-align: center;
    align-items: center;
    justify-content: center;
  }
  .footer {
    text-align: center;
    margin-bottom: 12px;
    a {
      cursor: pointer;
      margin-left: 4px;
      text-decoration: underline;
    }
    a:hover {
      color: #888888;
    }
  }
}
</style>

<style scoped>
.v-card {
  padding: 32px;
}
.errorMessage {
  color: red;
  width: 100%;
  text-align: center;
}
</style>
