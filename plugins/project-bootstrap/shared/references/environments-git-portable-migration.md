# Environments, Git, Portability, and Migration

## Safe workspace

Before recursive inspection: resolve the intended workspace, enter it explicitly, verify the current root, and only then recurse. If the workspace cannot be confirmed, fail closed. Never scan a drive, home directory, or parent tree merely because a shell opened there.

## Environment Map

Record only material environments and capabilities: local workspace, other user environments, shared storage, servers, test/staging/production, or external services. Mutable facts must be refreshed from the actual environment when practical.

Complexity controls workflow depth. Participation controls user involvement. Authority and risk control permitted actions. Available capabilities control mechanism. The execution profile controls reasoning capacity.

## Git

Local Git, a remote provider, a connector, and host authentication are different states. Keep READ, CHANGE, COMMIT, PUBLISH, and INTEGRATE separate. Do not infer one from another or expose credentials.

Task Branch does not mean Git branch. Create a branch or worktree only when isolation is needed.

## PORTABLE

PORTABLE is optional. It means required project state is transferred, synchronized, or accessible so work can continue in another environment. It is not tied to removable storage. No portability need means no portable workflow.

## Migration

Migration is a deliberate source-to-destination transition, separate from an ordinary path or mount change. Use source preparation, destination receipt, and Master bootstrap only when a migration actually exists. No migration means no migration artifacts.
