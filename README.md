# Introduction to Microservices
## Date Time: 29-June-2023 at 09:00 AM IST
### Event URL:
### Youtube URL:
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/cfff5b6b-1743-405b-acaf-14b3bb9fada9)


## Prerequisites:
NA

## Software/Tools
1. Visual studio
2. GitHub Desktop
3. gitbash
4. Windows terminal 


## Languages:
1. C sharp(C#)

## Information

1. Creating a Console Application within an Existing and New folder
2. Creating a Console Application within a new folder
3. Creating a Console Application with .NET (6/7/8)
4. Creating a Console Application with .NET 6
5. Creating a Console Application with .NET 7
6. Creating a Console Application with .NET 8
7. Creating a Console Application with global.json inside folder
8. Creating a Console Application with .NET 6
9. Creating a Console Application with .NET 7
10. Creating a Console Application with .NET 8
11. Executing the Same Application in .NET 6/7/8
12. Execute Sample C# Code



## Creating Console Application using C#.


## 1. Creating a Console Application within an Existing and New folder.

### 1.1.  Creating a Console Application within an Existing folder.
> 
1. Create a folder existingfolder
2. Open cmd and navigate to existingfolder 
3. Run the below command
4. This will create a console application within the existingfolder
5. It will name the console application as existingfolder

```
dotnet new console
```
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/6d57014b-394b-49bf-a1a7-5a1fb885ea43)

## 1.2. Creating a Console Application within a new folder.
>
1. Execute the below command   
2. This will create a console application within the newfolder 
3. It will name the console application as newfolder

```
dotnet new console -o newfolder
dotnet new console -n "projectName"
dotnet new console -n "projectName" -o folderName
```

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/4e0f3c9f-0e24-49c2-a5a5-124b3c04d5b6)


The Project file name will be same as folder name.

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/c83a851e-4b17-46b3-aa33-3818b6f3b80e)


This will create the Porject file with different name.

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/9af19958-44b8-489d-adfa-f57183bc275d)


This will create project inside specified folder.

## 2. Viewing Compiler Version and Language Version.
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/2091be5b-3901-4784-8ec6-43b360f1d633)

## 3. Creating a Console Application with .NET (6/7/8).


### 3.1. Creating a Console Application with .NET 6.
```
dotnet new console -o demo3 -f net6.0
```

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/be2847d9-6cb6-4f8c-9237-0fb405e16d3b)


### 3.2.  a Console Application with .NET 7.
```
dotnet new console -o demo4 -f net7.
```

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/870a4f92-0c50-4707-9587-c9bcc435f1c3)

### 3.3. Creating a Console Application with .NET 8.
```
dotnet new console -o demo5 -f net8.0
```
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/20319131-e937-4d66-a031-70b8fe857d61)


## 4. Creating a Console Application with global.json inside folder.

> Execute the below command

``` dotnet new list
dotnet new globaljson --help
dotnet --list-sdks

dotnet new globaljson --sdk-version <VersionNumber> --dry-run
dotnet new globaljson --sdk-version <VersionNumber>
```

### 4.1. Creating a Console Application with .NET 6.
```
dotnet --list-sdks
dotnet new globaljson --sdk-version 6.0.408 --dry-run
dotnet new globaljson --sdk-version 6.0.408
dotnet new console -o demo6
```
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/178b542f-34b5-47d5-89c3-793540df6596)

### 4.2. Creating a Console Application with .NET 7.
```
dotnet --list-sdks
dotnet new globaljson --sdk-version 7.0.105 --dry-run
dotnet new globaljson --sdk-version 7.0.105
dotnet new console -o demo7
```

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/3d160a9a-0225-414f-8d93-cce4deef7963)

### 4.3. Creating a Console Application with .NET 8.
```
dotnet --list-sdks
dotnet new globaljson --sdk-version 8.0.100-preview.4.23260.5 --dry-run
dotnet new globaljson --sdk-version 8.0.100-preview.4.23260.5
dotnet new console -o demo8
```
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/a99d623d-35f5-4931-a660-0a2de7f3c9fb)

## 5. Executing the Same Application in .NET 6/7/8.
>
1. Execute the project in 6/7/8
2. View the output
### 5.1 . Sample C# Code.

```
// See https:// aka.ms/ new-console-template for more information
Console.WriteLine(Environment.CurrentDirectory);
Console.WriteLine(Environment.OSVersion.VersionString);
Console.WriteLine(Environment.Version);
Console.WriteLine(Environment.UserName);
Console.WriteLine(Environment.MachineName);
Console.WriteLine(Environment.ProcessorCount);
Console.WriteLine(Environment.SystemDirectory);
Console.WriteLine(Environment.UserDomainName);
Console.WriteLine(Environment.UserInteractive);
Console.WriteLine(Environment.WorkingSet);
Console.WriteLine(Environment.Is64BitOperatingSystem);
Console.WriteLine(Environment.Is64BitProcess);
```
![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/6c2e0911-14ab-4865-a8ea-8db60a91e21c)


Execute the .NET 6 project after writing above code.

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/bcdb8c19-64fa-4eea-956c-e6194be07f04)


Execute the .NET 7 project after writing above code.

![image](https://github.com/Ashutosh-Tech-Skillz-Academy/learn-csharp/assets/90964215/41fa4a5c-a945-4984-9baa-b8db99305626)


Execute the .NET 8 project after writing above code.
