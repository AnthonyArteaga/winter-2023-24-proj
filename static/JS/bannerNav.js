        // JavaScript for banner navigation
        let currentIndex = 0;
        const bannerContainer = document.querySelector('.banners');
        const totalBanners = document.querySelectorAll('.banner-text').length;

        function scrollBanners(direction) {
            const bannerWidth = bannerContainer.offsetWidth / totalBanners;

            if (direction === 'left') {
                currentIndex = (currentIndex - 1 + totalBanners) % totalBanners;
            } else if (direction === 'right') {
                currentIndex = (currentIndex + 1) % totalBanners;
            }

            const translateValue = -currentIndex * bannerWidth;
            bannerContainer.style.transform = `translateX(${translateValue}px)`;
        }