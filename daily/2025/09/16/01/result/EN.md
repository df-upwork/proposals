1) Your website is running on Magento 2.4: https://www.mamartialarts.com/magento_version
2) Judging by the fact that the failure occurs specifically on line 75, the exact version of your website is between 2.4.4 and 2.4.6 (in other versions of the 2.4 branch, the failure will occur on a different line).
3) The exact failure point: https://github.com/magento/magento2/blob/2.4.6/lib/internal/Magento/Framework/App/AreaList.php#L75
This is the line `if (isset($areaInfo['frontName']) && $areaInfo['frontName'] === $frontName) {`
4) The low-level cause of the failure: the `$areaInfo` variable is `NULL`.
5) Since `$areaInfo` is an element of the `$this->_areas` array, the fundamental problem is that the area configuration array (`_areas`) contains `NULL` instead of the expected area configuration data array.
6) The `_areas` array is populated through the Dependency Injection (DI) mechanism based on the merged configuration of all modules (`di.xml`).
7) The most likely high-level reasons leading to the low-level reason from point 4:
7.1) Incorrect configuration of a third-party module (an error in `di.xml`).
A third-party module may incorrectly define the arguments for the `AreaList` constructor in its `di.xml` file when trying to add or change an area configuration, which leads to the injection of `NULL`.
This is a direct mechanism that affects the contents of `_areas`.
In my experience, DI configuration errors are common, especially in low-quality third-party modules.
If the problem occurred after installing/updating a module, this cause is very likely.
7.2) A caching failure.
In my experience, this cause is also common, however, it is too obvious.
It is possible that the caching on your server is configured in a non-trivial way.
7.3) A failure or interruption of the compilation process (Generated Code)
If the compilation process (`setup:di:compile`) was interrupted (e.g., due to a lack of memory or a timeout) or completed with an error, the files in the `generated/` directory may contain incomplete or corrupted DI configuration data.
An incomplete compilation leaves the system in an unstable state, which can lead to the incorrect initialization of classes, including `AreaList`.
8) The reasons you are suggesting (such as «Fix URL rewrite / .htaccess (or Nginx) so links resolve correctly») — are most likely irrelevant to your problem.
---
I have completed 536 projects (mostly Magento) here on Upwork.
I have created 127 open-source modules for Magento 2: https://github.com/topics/mage2pro-module-ready
I am the creator of https://mage2.pro?order=views
My primary GitHub profile: https://github.com/dmitrii-fediuk
My secondary GitHub profile (with some of my Magento modules): https://github.com/mage2pro
My website about non-Magento technologies: https://df.tips?order=views