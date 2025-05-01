import streamlit as st
from pages.modules.apply_css import setup_page
import json

def show_ab_page():
    st.markdown("<div class='page-title'>ABILITIES</div>", unsafe_allow_html=True)
    
    data = load_data()
    
    all_tags = set()
    for item_name, item_data in data.items():
        if 'tags' in item_data and isinstance(item_data['tags'], list):
            all_tags.update(item_data['tags'])
    
    # Добавим пустой тег для отображения всех предметов
    all_tags = sorted(list(all_tags))
    

    search_col, main_col = st.columns([2, 8])
    
    # Панель поиска слева
    with search_col:
        st.markdown("<div class='sidebar-panel'>", unsafe_allow_html=True)
        
        # Search
        st.markdown("<div class='sidebar-search'>", unsafe_allow_html=True)
        search_term = st.text_input("", placeholder="Search...", label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Tags
        st.markdown("<h4 class='sidebar-subtitle'>Tags</h4>", unsafe_allow_html=True)
        selected_tags = st.multiselect("Filter by tags", all_tags, label_visibility="collapsed")

        # Price filter
        min_price = min([item.get('price', 0) for item in data.values()]) if data else 0
        max_price = max([item.get('price', 0) for item in data.values()]) if data else 10000
        # Price range
        st.markdown("<h4 class='sidebar-subtitle'>Price range</h4>", unsafe_allow_html=True)
        price_range = st.slider(
            "Price",
            min_value=min_price,
            max_value=max_price,
            value=(min_price, max_price),
            step=100,
            label_visibility="collapsed"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Основной контент с карточками справа
    with main_col:
        # Фильтрация данных по поисковому запросу и тегам
        filtered_items = {}
        for item_name, item_data in data.items():
            # Проверка соответствия поисковому запросу
            name_match = search_term.lower() in item_name.lower()
            desc_match = 'description' in item_data and search_term.lower() in item_data['description'].lower()
            
            # Проверка соответствия тегам
            tags_match = True
            if selected_tags:
                item_tags = item_data.get('tags', [])
                tags_match = all(tag in item_tags for tag in selected_tags)
            
            # Проверка ценового диапазона
            price = item_data.get('price', 0)
            price_match = price_range[0] <= price <= price_range[1]
            
            # Добавление элемента в отфильтрованный список
            if (name_match or desc_match) and tags_match and price_match:
                filtered_items[item_name] = item_data
        
        # Отображение количества найденных элементов
        st.markdown(f"<div class='results-count'>Found: {len(filtered_items)} abilities</div>", unsafe_allow_html=True)
        
        # Отображение карточек в сетке
        if filtered_items:
            items_per_row = 3 
            
            items_list = list(filtered_items.items())
            item_groups = [items_list[i:i+items_per_row] for i in range(0, len(items_list), items_per_row)]
            
            for group in item_groups:
                cols = st.columns(items_per_row)
                
                for i, (item_name, item_data) in enumerate(group):
                    with cols[i]:
                        display_ability_card(item_name, item_data)
        else:
            st.markdown("<div class='empty-results'>No abilities found matching your search filters.</div>", unsafe_allow_html=True)

def display_ability_card(item_name, item_data):
    TagColors = {
    "Ability Power" : "violet",
    "Health" : "white",
    "Weapon power": "red",
    "Ability Lifesteal": "yellow",
    "Cooldown Reduction": "blue",
    "Hero item": "cian",
    "Armor": "white",
    "Attack Speed":"orange",
    "Shields": "white",
    "Move Speed": "green",
    "Melee Damage": "white",
    "Weapon Lifesteal": "yellow",
}
    # Формируем HTML для отображения тегов
    tags_html = ""
    if 'tags' in item_data and item_data['tags']:
        for tag in item_data['tags']:
            tags_html += f'<span class="tag" style="color: {TagColors.get(tag, "gray")};">{tag}</span>'
    
    image_path = item_data.get('image', '')
    image_html = ""
    if image_path:
        image_html = f'<div class="ability-card-image"><img src="{image_path}" alt="{item_name}"></div>'
    
    card_html = f"""
    <div class="ability-card">
        {image_html}
        <div class="ability-card-header">
            <h3>{item_name}</h3>
            <div class="price-tag">{item_data.get('price', 'N/A')}</div>
        </div>
        <div class="ability-card-body">
            <p>{item_data.get('description', 'No description')}</p>
        </div>
        <div class="ability-card-tags">
            {tags_html}
        </div>
    </div>
    """
    
    # Отображаем карточку
    st.markdown(card_html, unsafe_allow_html=True)

def load_data():
    try:
        with open('pages/modules/powers.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return {}

def add_custom_css():
    """
    Добавляет пользовательские стили CSS
    """
    st.markdown("""
    <style>

    .page-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    

    .search-panel {
        background-color: #1e1e1e;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        position: sticky;
        top: 4rem;
    }
    

    .search-panel .stTextInput, 
    .search-panel .stMultiSelect,
    .search-panel .stSlider {
        width: 100%;
    }
    

    .search-panel > div {
        margin-bottom: 1rem;
    }
    

    .ability-card {
        margin: 0.5rem;
        background-color: #2a2a2a;
        border-radius: 10px;
        padding: 1.25rem;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        display: flex;
        flex-direction: column;
        border: 1px solid #3a3a3a;
    }
    
    .ability-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
        border-color: #4a4a4a;
    }
    
    .ability-card-image {
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .ability-card-image img {
        max-height: 80px;
        max-width: 100%;
        object-fit: contain;
    }
    
    .ability-card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.75rem;
        border-bottom: 1px solid #3a3a3a;
        padding-bottom: 0.75rem;
    }
    
    .ability-card-header h3 {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
    }
    
    .ability-card-body {
        flex-grow: 1;
        color: #cccccc;
        font-size: 0.9rem;
        line-height: 1.4;
        margin-bottom: 1rem;
    }
    
    .price-tag {
        background-color: #ff9800;
        color: #000000;
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    
    .ability-card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .tag {
        background-color: #3a3a3a;
        color: #c0c0c0;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.7rem;
        white-space: nowrap;
    }
    
    .results-count {
        color: #aaaaaa;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        text-align: right;
    }
    
    .empty-results {
        text-align: center;
        padding: 3rem;
        color: #888888;
        background-color: #1e1e1e;
        border-radius: 10px;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="BOW2 - Abilities", layout="wide")
    setup_page(page_name="abilities")
    add_custom_css() 
    show_ab_page()