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

NO PORTABILITY NEED → NO PORTABLE CREDENTIALS WORKFLOW.

NO AUTHENTICATED SERVICE → NO CREDENTIAL STORAGE DISCUSSION.

Discuss a portable credential strategy only when portability is relevant, an authenticated external service is required, credential availability or placement affects the next work, and no still-applicable accepted credential strategy exists. If the accepted strategy still works in the current environment and access is available, verify access and do not reopen the decision.

Project Bootstrap 0.1.7 supports exactly two conceptual strategies:

1. credentials configured separately on each machine;
2. credentials stored with the portable working environment but outside Git.

Do not silently collapse this choice into machine-local credentials. Participation determines whether the user chooses explicitly or Project Bootstrap may choose a safe reversible strategy within existing authority. Do not expose GitHub CLI, credential-manager, or other mechanism details before they are needed for the strategy decision.

Do not standardize an encrypted credential store. Reopen the strategy only after a material change such as a new environment, unavailable required access, a new authenticated service, an existing strategy that no longer satisfies portability, materially changed risk, or materially changed authority.

Durable state may record only non-secret facts: whether access is available, whether the strategy is machine-local or portable, the expected mechanism or location without secret values, and non-secret recovery or revocation information. Prefer relative portable paths when practical instead of fixed drive letters.

## Migration

Migration is a deliberate source-to-destination transition, separate from an ordinary path or mount change. Use source preparation, destination receipt, and Master bootstrap only when a migration actually exists. No migration means no migration artifacts.
