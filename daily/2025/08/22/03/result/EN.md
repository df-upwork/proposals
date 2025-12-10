1) The cause of your problem is obvious to me — it is the change in CommonJS/ESM interoperability: the «`.default` problem».
The JavaScript ecosystem is currently transitioning from CommonJS (which uses require) to ES Modules (ESM, which uses import/export).
When TypeScript compiles ESM to CommonJS, the default export (`export default`) is often placed in the `.default` property of the resulting object.
If the code expects to receive a function directly through `require('module')`, but receives `{default: function}`, an attempt to call `require('module')()` results in «TypeError: require(...) is not a function».
Simply put, code that previously executed successfully as `require('module')()`, now does not work because `require('module')` returns not a function, but a Module Namespace Object.
The expected function is likely located in the `.default` property.
2) The most likely reasons why the problem arose specifically after the Node.js version upgrade:
2.1) The TypeScript configuration (`tsconfig.json`) was not adapted to the new Node.js version, which led to a change in the structure of the compiled code or incorrect module resolution.
2.2) A dependency was updated that changed its export method (e.g., switched to ESM), and the current project configuration cannot process it correctly.
---
My GitHub profile: https://github.com/dmitrii-fediuk