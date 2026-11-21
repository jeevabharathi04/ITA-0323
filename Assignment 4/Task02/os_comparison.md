# Task 02: Architectural Comparison — Android vs iOS vs Windows Phone/UWP

| Architectural Dimension | Android (Google) | iOS (Apple) | Windows (UWP / WinRT) |
| :--- | :--- | :--- | :--- |
| **Base Kernel** | Monolithic Linux Kernel with custom drivers (Binder, LMK). | Hybrid XNU Kernel (Mach microkernel + FreeBSD core). | Windows NT Hybrid Microkernel. |
| **Application Runtime** | Android Runtime (ART) executing optimized DEX bytecode (AOT + JIT). | Native ARM64 Mach-O binaries compiled via LLVM / Clang (Zero VM). | .NET Native / CoreCLR executing Common Intermediate Language (CIL). |
| **IPC Mechanism** | **Binder:** Linux kernel character device `/dev/binder` with ioctl and RPC. | **XPC / Mach Messages:** High-performance microkernel Mach ports and serialization. | **COM (Component Object Model) / RPC:** WinRT language projection boundaries. |
| **Graphics Subsystem** | SurfaceFlinger compositor with Hardware Composer (HWC) and Skia/Vulkan. | Quartz Compositor / Core Animation directly coupled to Metal API. | Desktop Window Manager (DWM) with DirectX rendering pipelines. |
| **App Sandboxing** | Multi-User Linux Isolation (unique UID per app, SELinux policies). | Containerized App Sandbox with Seatbelt kernel policy enforcement. | AppContainer with SID-based restricted security tokens. |
| **Distribution Control** | Open (Google Play, sideloading APKs, alternative app stores). | Walled Garden (Mandatory App Store curation, code-signing enforcement). | Microsoft Store (optional developer enterprise sideloading). |
