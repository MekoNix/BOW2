import streamlit as st
import os

def get_resource_path(relative_path):
    """
    Функция для поиска правильного пути к файлу ресурса
    Args:
        relative_path (str): Относительный путь к файлу
    Returns:
        str: Полный путь к файлу
    """
    try:
        # Получаем путь к текущему файлу
        base_path = os.path.dirname(os.path.abspath(__file__))
        # Поднимаемся на три уровня вверх (из modules/pages в корень проекта)
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(base_path)))
        # Собираем полный путь
        full_path = os.path.join(root_path, "project", "webapp", relative_path)
        
        # Проверяем существование файла
        if os.path.exists(full_path):
            return full_path
        else:
            raise exit()        
    except Exception as e:
        st.error(f"Ошибка при поиске файла: {str(e)}")

