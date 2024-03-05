<template>
  <div class="cardContainer">
    <div class="img-container">
      <img :src="info.imgName" />
    </div>
    <div class="details">
      <!-- <div class="trail-level">
        <span>{{ info.level }}</span>
        <span>•</span>
        <span>
          <v-icon name="fa-star" color="rgb(100, 246, 123)" />
          {{ info.score }}
        </span> -->
      <!-- <span class="comments-number">({{ info.commentsNum }})</span> -->
      <!-- </div> -->
      <div class="trail-basic">#{{ index + 1 }} - {{ info.trailName }}</div>
      <div class="trail-level">
        <div class="trail-level-details">
          <v-icon
            class="trail-level-icon"
            name="bi-circle-fill"
            color="rgb(100, 246, 123)"
          />
          <span>{{ info.green }}</span>
        </div>
        <div class="trail-level-details">
          <v-icon
            class="trail-level-icon"
            name="bi-square-fill"
            color="#0077B6"
          />
          <span>{{ info.blue }}</span>
        </div>
        <div class="trail-level-details">
          <v-icon
            class="trail-level-icon"
            name="bi-diamond-fill"
            color="#111111"
          />
          <span>{{ info.diamond }}</span>
        </div>
        <div class="trail-level-details">
          <div class="trail-level-icon doubleDiamond">
            <v-icon name="bi-suit-diamond-fill" color="#111111" />
            <v-icon name="bi-suit-diamond-fill" color="#111111" />
          </div>
          <span>{{ info.doubleDiamond }}</span>
        </div>
      </div>
      <div class="park-basic">{{ info.parkName }}</div>
      <div class="trail-length">
        Trail Length: {{ info.length }}
        <!-- • est. {{ info.est }} -->
      </div>
      <!-- <div class="trail-description">
        <span>{{ info.desctiption }}</span>
      </div>
      <a class="showmore-btn" href="http://google.com">Show More</a> -->
    </div>
    <div @click.stop="changeBookmarkStatus(info)">
      <v-icon class="bookmarked" v-if="info.isBookmarked" name="fa-bookmark" />
      <v-icon class="unbookmark" v-else name="fa-regular-bookmark" />
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  info: Object,
  index: Number
})
const changeBookmarkStatus = (info) => {}
</script>

<style lang="less" scoped>
.cardContainer {
  display: grid;
  grid-template-columns: 1fr 5fr;
  column-gap: 20px;
  height: 180px;
  position: relative;
  .img-container {
    width: 260px;
    height: 180px;
    overflow: hidden;
    border-radius: 6px;
    img {
      width: 100%;
      height: 100%;
      justify-self: end;
    }
    img:hover {
      transform: scale(1.1);
      transition: transform 0.3s;
    }
  }
  .details {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-size: 16px;
    max-width: 800px;
    .trail-level {
      display: flex;
      align-items: center;
      margin-bottom: 8px;
      gap: 6px;
    }
    .comments-number,
    .park-basic,
    .trail-length {
      font-size: 14px;
      color: #888888;
    }
    .trail-basic {
      font-size: 18px;
      font-weight: bold;
    }
    .park-basic {
      text-decoration: underline;
    }
    .trail-length {
      margin-bottom: 16px;
    }
    .trail-description {
      font-size: 14px;
      color: #444444;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      line-height: 20px;
      max-height: 40px;
      overflow: hidden;
      position: relative;
    }
    .showmore-btn {
      color: #444;
      font-weight: bolder;
      font-size: 10px;
    }
    .trail-level {
      gap: 18px;
      .trail-level-details {
        display: flex;
        align-items: center;
        .trail-level-icon {
          width: 36px;
          text-align: center;
        }
        .doubleDiamond {
          :first-child {
            margin-right: -9px;
          }
        }
      }
    }
  }
  .unbookmark,
  .bookmarked {
    position: absolute;
    right: 0;
    top: 0;
    width: 24px;
    height: 24px;
  }
  .unbookmark {
    color: #444444;
  }
  .bookmarked {
    color: rgb(100, 246, 123);
  }
}
</style>
