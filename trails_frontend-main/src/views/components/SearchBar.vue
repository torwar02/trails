<template>
  <div class="search-bar">
    <div class="options">
      <!-- difficulty -->
      <v-select
        class="selections"
        v-model="selectedDifficulty"
        :items="difficulty"
        label="Difficulty"
        variant="outlined"
        multiple
      >
        <template v-slot:selection="{ item, index }">
          <v-chip v-if="index < 2">
            <span>{{ item.title }}</span>
          </v-chip>
          <span
            v-if="index === 2"
            class="text-grey text-caption align-self-center"
          >
            +{{ selectedDifficulty.length - 2 }}
          </span>
        </template>
      </v-select>
      <!-- suitability -->
      <v-select
        class="selections"
        v-model="selectedSuitability"
        :items="suitability"
        label="Suitability"
        variant="outlined"
        multiple
      >
        <template v-slot:selection="{ item, index }">
          <v-chip v-if="index < 1">
            <span>{{ item.title }}</span>
          </v-chip>
          <span
            v-if="index === 1"
            class="text-grey text-caption align-self-center"
          >
            +{{ selectedSuitability.length - 1 }}
          </span>
        </template>
      </v-select>
      <!-- rating -->
      <v-select
        class="selections"
        v-model="selectedRatings"
        :items="ratings"
        label="Ratings"
        variant="outlined"
      >
        <template v-slot:selection="{ item }">
          <v-chip class="selected-ratings">
            <v-icon
              class="star-icon"
              name="fa-star"
              color="rgb(100, 246, 123)"
            />
            <span>{{ item.title }}</span>
          </v-chip>
        </template>
      </v-select>
    </div>
    <div class="searchBox"></div>
    <div class="btns">
      <v-btn class="btn btn-search" @click="search">Search</v-btn>
      <v-btn class="btn btn-reset" @click="reset">Reset</v-btn>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const difficulty = ref(['Easy', 'Medium', 'Hard'])
const suitability = ref([
  'Dog friendly',
  'Kid friendly',
  'Wheelchair friendly',
  'Stroller friendly',
  'Paved',
  'Partially Paved'
])
const ratings = ref([
  'All',
  '1.0 and Up',
  '2.0 and Up',
  '3.0 and Up',
  '4.0 and Up',
  '5.0'
])
const allDistances = {
  0: '5 mi',
  1: '10',
  2: '15',
  3: '20',
  4: '25',
  5: '30+'
}

const selectedDifficulty = ref([])
const selectedSuitability = ref([])
const selectedRatings = ref([])
const distances = ref([0, 30])
const search = () => {}
const reset = () => {
  selectedDifficulty.value = []
  selectedSuitability.value = []
  selectedRatings.value = []
}
defineExpose({ reset })
</script>

<style lang="less" scoped>
.search-bar {
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 80%;
  padding: 20px 80px;
  border-bottom: 1px solid #eeeeee;
  .options {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    .selections {
      width: 215px;
      .selected-ratings {
        display: flex;
        align-items: center;
        .star-icon {
          padding-bottom: 2px;
        }
      }
    }
    .sliders {
      width: 380px;
    }
  }
  .btns {
    display: flex;
    align-items: center;
    gap: 32px;
    .btn {
      width: 100px;
    }
  }
}
</style>

<style lang="less">
.options {
  .v-field.v-field--appended {
    .v-field__append-inner {
      display: none;
    }
  }
}
</style>
