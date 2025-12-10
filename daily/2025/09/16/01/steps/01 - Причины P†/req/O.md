# 0.
Сегодня 2025-09-16.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021967619521290809716

## 2.2. Title
Magento 2 – Fix Broken Links / URL Rewrite Error

## 2.3. Description
`PD` ≔ 
```text
My Magento 2 website (mamartialarts.com) is showing errors when users click product or category links (e.g., sparring-gear.html). The error is:
Exception #0 (Exception): Notice: Trying to access array offset on value of type null
in /vendor/magento/framework/App/AreaList.php on line 75

I need a Magento expert to:
• Fix URL rewrite / .htaccess (or Nginx) so links resolve correctly
• Verify Use Web Server Rewrites = Yes and Base URLs are correct
• Rebuild URL rewrites, reindex catalog, and flush caches
• Disable error display in production so customers don’t see stack traces
• Provide a short before/after verification (links tested)
What I’m Looking For
• Strong experience fixing Magento 2 URL rewrite and routing issues
• Ability to start immediately and resolve quickly
• Clear communication and short report once fixed

⸻

Questions for You
• Have you fixed Magento 2 AreaList/URL rewrite errors before?
• What is your approach to resolving this?
• How soon can you start?

⸻

⚡ Note: Please include relevant examples of similar Magento fixes in your proposal.
```

## 2.4. Tags
Magento

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Annandale

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Sep 8, 2019
### 5.3.2. Hire rate (%)
90
### 5.3.3. Количество опубликованных проектов (jobs posted)
10
### 5.3.4. Total spent (USD)
390 
### 5.3.5. Количество оплаченных часов в почасовых проектах
3
### 5.3.6. Средняя почасовая ставка (USD)
12.5

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
Trying to access array offset on value of type null
in /vendor/magento/framework/App/AreaList.php on line 75
~~~
```

# 10.
Метод сбоя `P†`:
```php
public function getCodeByFrontName($frontName)
{
	foreach ($this->_areas as $areaCode => &$areaInfo) {
		if (!isset($areaInfo['frontName']) && isset($areaInfo['frontNameResolver'])) {
			$resolver = $this->_resolverFactory->create($areaInfo['frontNameResolver']);
			$areaInfo['frontName'] = $resolver->getFrontName(true);
		}
		if (isset($areaInfo['frontName']) && $areaInfo['frontName'] === $frontName) {
			return $areaCode;
		}
	}
	return $this->_defaultAreaCode;
}
```
https://github.com/magento/magento2/blob/2.4.0/lib/internal/Magento/Framework/App/AreaList.php
 