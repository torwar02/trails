<template>
  <div class="nav-container">
    <!-- logo -->
    <div class="logo">
      <router-link to="/" class="router-link">⛰️ All Trails</router-link>
    </div>
    <!-- nav items -->
    <div class="nav-items">
      <router-link to="/recommdation" class="router-link">
        Recommdation
      </router-link>
      <router-link to="/nationalParkList" class="router-link">
        Explore
      </router-link>
      <router-link to="/saved" class="router-link">Saved</router-link>
      <router-link to="/PhotoShop" class="router-link"> PhotoShop </router-link>
    </div>
    <!-- User info  -->
    <div class="user">
      <v-btn v-if="!isLoggedin">
        Log in
        <v-dialog v-model="isSignDialogShow" activator="parent" class="dialog">
          <sign-dialog
            :showLogin="dialogShowLogin"
            @closeDialog="isSignDialogShow = false"
            @loginSuccess="authorized"
          ></sign-dialog>
        </v-dialog>
      </v-btn>
      <v-avatar
        v-else
        class="avatar"
        @mouseover="isMenuShow = true"
        @mouseleave="isMenuShow = false"
        id="menu-activator"
      >
        <span class="text-h7">{{ initials }}</span>
      </v-avatar>
      <div
        class="menu"
        v-show="isMenuShow"
        @mouseover="isMenuShow = true"
        @mouseleave="isMenuShow = false"
      >
        <v-list>
          <v-list-item v-for="(item, index) in personalSpace" :key="index">
            <v-list-item-title @click="optionHandler(item)">
              {{ item.title }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import SignDialog from './SignDialog.vue'

const router = useRouter()
const dialogShowLogin = ref('true')
const isLoggedin = ref(false)
const isMenuShow = ref(false)
const isSignDialogShow = ref(false)
const initials = ref('JD')

const personalSpace = [
  { title: 'Profile', path: '/Profile' },
  { title: 'Settings', path: '/Settings' },
  { title: 'Logout', path: '/', isLoggingout: true }
]
const optionHandler = (item) => {
  isMenuShow.value = false
  if (item.isLoggingout) {
    isLoggedin.value = false
  }
  router.push(item.path)
}
const authorized = (userData) => {
  const { firstname, lastname } = userData
  initials.value = firstname[0] + lastname[0]
  isSignDialogShow.value = false
  isLoggedin.value = true
}
</script>

<style lang="less" scoped>
@import '../../assets/styles/colors.less';
.nav-container {
  height: 64px;
  width: 100%;
  display: flex;
  align-items: center;
  background-color: @grey-lighten-5;
  border-bottom: 1px @grey-lighten-3 solid;
  .logo {
    text-align: right;
    min-width: 160px;
    font-size: 24px;
  }
  .nav-items {
    width: 100%;
    display: flex;
    padding: 0 48px;
    gap: 32px;
  }
  .user {
    min-width: 160px;
    text-align: center;
    vertical-align: middle;
    position: relative;
    .avatar {
      width: 36px;
      height: 36px;
      background-color: @green-accent-2;
      cursor: pointer;
      color: @grey-darken-3;
    }
    .avatar:hover {
      background-color: @green-accent-3;
      transition: all 0.3s;
    }
    .menu {
      box-shadow: 0 4px 8px -2px rgba(0, 0, 0, 0.3);
      position: absolute;
      right: 54px;
      top: 36px;
    }
  }
  .router-link {
    color: @grey-darken-4;
    text-decoration: none;
  }
}
</style>

<style scoped>
.v-list-item {
  width: 180px;
  text-align: left;
  cursor: pointer;
}
.v-list-item:hover {
  background-color: #eeeeee;
  transition: all 0.3s;
}
</style>
