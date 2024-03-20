<template>
  <div class="outerContainer">
    <div class="innerContainer">
      <div class="fileContainer">
        <v-file-input
          class="inputBox"
          label="File input of Selfie"
        ></v-file-input>
        <img src="../assets/selfie.png" alt="" width="300px" height="200px" />
      </div>
      <div class="plus">+</div>
      <div class="fileContainer">
        <v-select
          label="Select"
          :items="[
            'Glacier',
            'Grand Canyon',
            'Grand Teton',
            'Great Basin',
            'Great Smokey'
          ]"
        ></v-select>
        <img
          src="../assets/grandcanyon.jpg"
          alt=""
          width="300px"
          height="200px"
        />
      </div>
    </div>
    <div class="plus">=</div>
    <div class="photoContainer">
      <img
        src="../assets/photoShopped.jpg"
        alt=""
        width="600px"
        height="400px"
      />
    </div>
  </div>
</template>

<script setup></script>

<style lang="less" scoped>
.outerContainer {
  width: 80%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  .innerContainer {
    display: flex;
    align-items: center;
    .fileContainer {
      display: flex;
      flex-direction: column;
      width: 300px;
      .inputBox {
        margin-left: -40px;
      }
    }
  }
  .plus {
    font-size: 32px;
    vertical-align: middle;
    text-align: center;
    padding: 24px;
    padding-top: 36px;
  }
  .photoContainer {
    width: 600px;
    height: 400px;
  }
}
</style>
