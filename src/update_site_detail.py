with open('hongtu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到需要替换的位置
old_end = '''        function goBackHero() {
            switchPage(previousPage);
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;'''

new_end = '''        function goBackHero() {
            switchPage(previousPage);
        }

        let currentSite = null;

        function openSiteDetail(siteId) {
            currentSite = redSites.find(s =&gt; s.id === siteId);
            if (!currentSite) return;

            previousPage = 'mapPage';
            document.getElementById('siteDetailTitle').textContent = currentSite.name;

            const contentContainer = document.getElementById('siteDetailContent');

            let heroImage = currentSite.images &amp;&amp; currentSite.images.length &gt; 0 ? currentSite.images[0] : null;
            let heroHtml = '';

            if (heroImage) {
                heroHtml = `
                    &lt;div class="site-detail-hero"&gt;
                        &lt;img src="${heroImage}" alt="${currentSite.name}"&gt;
                        &lt;div class="site-detail-hero-overlay"&gt;
                            &lt;h1&gt;${currentSite.name}&lt;/h1&gt;
                            &lt;p&gt;主要人物：${currentSite.hero}&lt;/p&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                `;
            } else {
                heroHtml = `
                    &lt;div class="site-detail-hero"&gt;
                        &lt;div class="site-detail-hero-overlay"&gt;
                            &lt;h1&gt;${currentSite.name}&lt;/h1&gt;
                            &lt;p&gt;主要人物：${currentSite.hero}&lt;/p&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                `;
            }

            let detailHtml = '';
            if (currentSite.detail) {
                detailHtml = `
                    &lt;div class="site-detail-section"&gt;
                        &lt;div class="site-detail-section-title"&gt;
                            &lt;i class="ri-information-line"&gt;&lt;/i&gt;
                            景点介绍
                        &lt;/div&gt;
                        &lt;p class="site-detail-text"&gt;${currentSite.detail}&lt;/p&gt;
                    &lt;/div&gt;
                `;
            }

            let historyHtml = '';
            if (currentSite.history) {
                historyHtml = `
                    &lt;div class="site-detail-section"&gt;
                        &lt;div class="site-detail-section-title"&gt;
                            &lt;i class="ri-book-open-line"&gt;&lt;/i&gt;
                            历史记录
                        &lt;/div&gt;
                        &lt;p class="site-detail-text"&gt;${currentSite.history}&lt;/p&gt;
                    &lt;/div&gt;
                `;
            }

            let imagesHtml = '';
            if (currentSite.images &amp;&amp; currentSite.images.length &gt; 0) {
                let imgTags = currentSite.images.map(img =&gt; `
                    &lt;div class="site-detail-image"&gt;
                        &lt;img src="${img}" alt="景点图片"&gt;
                    &lt;/div&gt;
                `).join('');
                imagesHtml = `
                    &lt;div class="site-detail-section"&gt;
                        &lt;div class="site-detail-section-title"&gt;
                            &lt;i class="ri-image-line"&gt;&lt;/i&gt;
                            景点图集
                        &lt;/div&gt;
                        &lt;div class="site-detail-images"&gt;
                            ${imgTags}
                        &lt;/div&gt;
                    &lt;/div&gt;
                `;
            }

            const navHtml = `
                &lt;div class="site-nav-section"&gt;
                    &lt;div class="site-detail-section-title"&gt;
                        &lt;i class="ri-navigation-line"&gt;&lt;/i&gt;
                        导航系统
                    &lt;/div&gt;
                    &lt;div class="site-nav-modes"&gt;
                        &lt;div class="site-nav-mode active" data-mode="driving" onclick="selectSiteNavMode(this)"&gt;
                            &lt;i class="ri-car-line"&gt;&lt;/i&gt;
                            &lt;span&gt;打车&lt;/span&gt;
                        &lt;/div&gt;
                        &lt;div class="site-nav-mode" data-mode="driving" onclick="selectSiteNavMode(this)"&gt;
                            &lt;i class="ri-car-line"&gt;&lt;/i&gt;
                            &lt;span&gt;驾车&lt;/span&gt;
                        &lt;/div&gt;
                        &lt;div class="site-nav-mode" data-mode="transfer" onclick="selectSiteNavMode(this)"&gt;
                            &lt;i class="ri-bus-line"&gt;&lt;/i&gt;
                            &lt;span&gt;公交&lt;/span&gt;
                        &lt;/div&gt;
                        &lt;div class="site-nav-mode" data-mode="walking" onclick="selectSiteNavMode(this)"&gt;
                            &lt;i class="ri-walk-line"&gt;&lt;/i&gt;
                            &lt;span&gt;步行&lt;/span&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                    &lt;button class="site-nav-btn" onclick="startSiteNavigation()"&gt;
                        &lt;i class="ri-navigation-line"&gt;&lt;/i&gt;
                        开始导航
                    &lt;/button&gt;
                &lt;/div&gt;
            `;

            contentContainer.innerHTML = heroHtml + detailHtml + historyHtml + imagesHtml + navHtml;

            addToBrowseHistory(currentSite, 'site');
            switchPage('siteDetailPage');
        }

        function selectSiteNavMode(el) {
            document.querySelectorAll('.site-nav-mode').forEach(m =&gt; m.classList.remove('active'));
            el.classList.add('active');
            currentRouteMode = el.getAttribute('data-mode');
        }

        function startSiteNavigation() {
            if (!currentSite) return;
            goBackSite();
            setTimeout(() =&gt; {
                planRoute(currentSite.lng, currentSite.lat, currentSite.name);
            }, 300);
        }

        function goBackSite() {
            switchPage(previousPage);
        }
    &lt;/script&gt;

    &lt;style&gt;
        .site-detail-hero {
            height: 200px;
            background: linear-gradient(135deg, var(--red-primary) 0%, var(--red-dark) 100%);
            position: relative;
            overflow: hidden;
        }

        .site-detail-hero img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.8;
        }

        .site-detail-hero-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 20px;
            background: linear-gradient(transparent, rgba(0,0,0,0.7));
            color: #fff;
        }

        .site-detail-hero-overlay h1 {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .site-detail-hero-overlay p {
            font-size: 14px;
            opacity: 0.9;
        }

        .site-detail-section {
            padding: 20px;
            border-bottom: 8px solid var(--bg-light);
        }

        .site-detail-section:last-child {
            border-bottom: none;
        }

        .site-detail-section-title {
            font-size: 18px;
            font-weight: bold;
            color: var(--red-primary);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .site-detail-section-title i {
            font-size: 22px;
        }

        .site-detail-text {
            font-size: 15px;
            line-height: 1.8;
            color: var(--text-dark);
        }

        .site-detail-images {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 15px;
        }

        .site-detail-image {
            aspect-ratio: 1;
            border-radius: 10px;
            overflow: hidden;
            background: var(--bg-light);
        }

        .site-detail-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .site-nav-section {
            padding: 20px;
            background: var(--bg-light);
        }

        .site-nav-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, var(--red-primary) 0%, var(--red-dark) 100%);
            color: #fff;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 4px 15px rgba(196, 30, 58, 0.3);
            transition: transform 0.2s;
        }

        .site-nav-btn:active {
            transform: scale(0.98);
        }

        .site-nav-btn i {
            font-size: 20px;
        }

        .site-nav-modes {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .site-nav-mode {
            flex: 1;
            padding: 12px 10px;
            background: #fff;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }

        .site-nav-mode.active {
            border-color: var(--red-primary);
            background: rgba(196, 30, 58, 0.1);
            color: var(--red-primary);
        }

        .site-nav-mode i {
            font-size: 22px;
            display: block;
            margin-bottom: 4px;
        }

        .site-nav-mode span {
            font-size: 12px;
        }
    &lt;/style&gt;
&lt;/body&gt;
&lt;/html&gt;'''

# 替换内容
new_content = content.replace(old_end, new_end)

with open('hongtu.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('File updated successfully!')
