# Установка из GitHub Plugin Marketplace

Импорт выполняет администратор ChatGPT workspace. Доступность пунктов интерфейса зависит от типа аккаунта, workspace и назначенной роли.

Используйте точные значения:

Source: `https://github.com/gipsy-teapsy/project-bootstrap`

Branch: `main`

Path: `<blank>`

`<blank>` означает: оставьте поле Path пустым, потому что `.agents/plugins/marketplace.json` находится в корне repository.

## Импорт

1. Откройте **Admin → Plugins**.
2. Выберите **Add → Import marketplace**.
3. Вставьте Source из блока выше.
4. Укажите Branch `main`.
5. Оставьте Path пустым; имя manifest вводить не нужно.
6. Нажмите **Import marketplace** и при запросе разрешите GitHub-доступ.
7. Откройте Import results и убедитесь, что появился **Project Bootstrap by Gipsy**.
8. Откройте plugin и настройте workspace installation policy для нужных ролей.
9. Установите **Project Bootstrap by Gipsy** из Plugins Directory и проверяйте его в новом чате.

Marketplace policy в repository задаёт `AVAILABLE` и `ON_INSTALL`, но при GitHub workspace import итоговые workspace policies настраивает администратор.

## Обновление

После push новой версии откройте **Admin → Plugins → Marketplaces**, выберите **Project Bootstrap by Gipsy** и нажмите **Sync now**. Проверьте сохранённый sync report. Невалидное обновление существующего plugin должно оставить последнюю рабочую версию; после исправления повторите **Sync now**.

## Ограничения текущей версии

Версия 0.1.0 не содержит MCP, Apps, OAuth или backend. ChatGPT marketplace import, cloud Manager, доступность в Codex и behavioral lifecycle пока не тестировались.
