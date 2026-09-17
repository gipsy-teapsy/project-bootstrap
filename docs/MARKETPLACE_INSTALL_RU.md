# Установка из GitHub Plugin Marketplace

Импорт выполняет администратор ChatGPT workspace. Доступность пунктов интерфейса зависит от типа аккаунта, workspace и назначенной роли.

Используйте точные значения:

Source: `https://github.com/gipsy-teapsy/project-bootstrap`

Branch: `main`

Path: `<blank>`

`<blank>` означает: оставьте поле Path пустым, потому что `.agents/plugins/marketplace.json` находится в корне repository.

## Импорт Plugin

1. Откройте **Admin → Plugins**.
2. Выберите **Add → Import marketplace**.
3. Вставьте Source из блока выше.
4. Укажите Branch `main`.
5. Оставьте Path пустым; имя manifest вводить не нужно.
6. Нажмите **Import marketplace** и при запросе разрешите GitHub-доступ.
7. Откройте Import results и убедитесь, что появился **Project Bootstrap**.
8. Откройте plugin и настройте workspace installation policy для нужных ролей.
9. Установите **Project Bootstrap** из Plugins Directory и проверяйте его в новом чате.

Marketplace policy в repository задаёт `AVAILABLE` и `ON_INSTALL`, но при GitHub workspace import итоговые workspace policies настраивает администратор.

## Cloud Manager в ChatGPT Project

Это отдельный способ доставки того же Manager contract для ChatGPT Project, где нельзя полагаться на прямую доступность Plugin Skills.

Один раз при создании Project:

1. Создайте ChatGPT Project.
2. Скачайте [CHATGPT_CLOUD_MANAGER.md](../plugins/project-bootstrap/docs/CHATGPT_CLOUD_MANAGER.md) из опубликованной версии.
3. Добавьте этот файл как источник Project.
4. Скопируйте только короткий activation stub из раздела **Project Instructions** artifact в Project Instructions.
5. Начните описывать проект обычными словами на своём языке.

Полный artifact или большой prompt в Project Instructions копировать не нужно. Cloud Manager не является четвёртой ролью и не заменяет Master/Task в workspace.

## Обновление

После push новой версии для marketplace откройте **Admin → Plugins → Marketplaces**, выберите **Project Bootstrap** и нажмите **Sync now**. Проверьте сохранённый sync report. Невалидное обновление существующего plugin должно оставить последнюю рабочую версию; после исправления повторите **Sync now**.

Для ChatGPT Project удалите старый `CHATGPT_CLOUD_MANAGER.md` и загрузите новый из той же опубликованной версии. Короткую Project Instructions меняйте только если release notes явно сообщают об изменении её схемы.

## Ограничения текущей версии

Версия 0.1.4 не содержит MCP, Apps, OAuth или backend. Наличие Cloud Manager artifact не доказывает доступность Plugin Skills в конкретной Cloud/Codex среде. Cloud Manager прошёл начальное ручное smoke testing; расширенный документированный behavioral suite продолжается в beta. ChatGPT marketplace Sync, доступность Plugin в Codex и полный behavioral lifecycle не заявлены как пройденные.
