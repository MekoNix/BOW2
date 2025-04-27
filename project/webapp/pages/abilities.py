import streamlit as st 
from pages.modules.apply_css import setup_page  
import json



def show_ab_page():
    # Применяем общие стили один раз в начале страницы
    st.markdown("""
    <style>
        .ability-card {
            background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
            border-radius: 15px;
            padding: 1rem;
            border: 1px solid #374151;
            margin-bottom: 1rem;
        }
        
        .main-content {
            padding-top: 5rem;
        }
        
        .ability-title {
            color: #f97316;
            margin-bottom: 0.5rem;
            font-size: 1.3rem;
            font-weight: bold;
        }
        
        .ability-description {
            color: #e5e7eb;
            font-size: 0.9rem;
        }
        
        .ability-tag {
            background-color: #374151;
            color: #f97316;
            padding: 5px 10px;
            border-radius: 20px;
            margin-right: 5px;
            font-size: 0.8rem;
            display: inline-block;
        }
        
        .ability-price {
            color: #f97316;
            font-weight: bold;
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    con_show()

def load_data():
    with open('pages/modules/powers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Функция для отображения карточки продукта
def display_product(name, description, image, tags, price):
    with st.container():
        # Используем класс для карточки
        st.markdown('<div class="ability-card">', unsafe_allow_html=True)
        
        # Изображение
        st.image(image, use_container_width=True)
        
        # Название
        st.markdown(f'<div class="ability-title">{name}</div>', unsafe_allow_html=True)
        
        # Описание
        st.markdown(f'<div class="ability-description">{description}</div>', unsafe_allow_html=True)
        
        # Теги
        tags_html = ' '.join([f'<span class="ability-tag">{tag}</span>' for tag in tags])
        st.markdown(f'<div style="margin: 0.5rem 0;">{tags_html}</div>', unsafe_allow_html=True)
        
        # Цена
        st.markdown(f'<div class="ability-price">{price} ₽</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def con_show():
    with st.container():
        st.markdown('<div class="main-content">', unsafe_allow_html=True)
        st.title("Способности героев Overwatch 2")
        st.markdown("Выберите способности для создания своего билда", 
                   help="Нажмите на карточку, чтобы узнать подробнее")
        st.markdown("---")
        
        # Загрузка данных
        products = load_data()
        product_items = list(products.items())
        
        # Отображение продуктов по 3 на строку
        for i in range(0, len(product_items), 3):
            cols = st.columns(3)
            for col, (name, details) in zip(cols, product_items[i:i+3]):
                with col:
                    display_product(
                        name=name,
                        description=details["description"],
                        image=details["image"],
                        tags=details["tags"],
                        price=details["price"]
                    )
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="BOW2 - Abilities", layout="wide")
    setup_page(page_name="abilities")    
    show_ab_page()